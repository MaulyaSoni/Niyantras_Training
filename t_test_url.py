from datetime import datetime

from database.schema import URL, ClickLog, URLStats
from operations.tasks import record_click_metrics


def test_short_links_are_unique(authenticated_client):
    response_1 = authenticated_client.post("/url",
        json={"url": "https://example.com/page-one"},
    )

    response_2 = authenticated_client.post("/url",
        json={"url": "https://example.com/page-two"},
    )

    assert response_1.status_code == 201
    assert response_2.status_code == 201

    short_link_1 = response_1.json()["short_link"]
    short_link_2 = response_2.json()["short_link"]

    assert short_link_1 != short_link_2


def test_short_url_redirects(client, created_url):
    response = client.get(
        f"/url/{created_url.short_link}",
        follow_redirects=False,
    )

    assert response.status_code == 303
    assert response.headers["location"] == created_url.url


def test_click_stats_are_counted_correctly(db, created_url):
    record_click_metrics(
        created_url.url_id,
        datetime.now(),
        "pytest",
    )

    record_click_metrics(
        created_url.url_id,
        datetime.now(),
        "pytest",
    )

    db.expire_all()

    url = db.get(URL, created_url.url_id)

    assert url is not None
    assert url.total_clicks == 2

    logs = (
        db.query(ClickLog)
        .filter(ClickLog.url_id == created_url.url_id)
        .all()
    )

    assert len(logs) == 2

    stats = (
        db.query(URLStats)
        .filter(URLStats.url_id == created_url.url_id)
        .all()
    )

    assert len(stats) == 1
    assert stats[0].clicks_per_day == 2