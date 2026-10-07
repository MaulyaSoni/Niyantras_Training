import requests

NATIONALIZE_API_URL = "https://api.nationalize.io"

COUNTRY_NAMES = {
    "IN": "India",
    "US": "United States",
    "GB": "United Kingdom",
    "CA": "Canada",
    "AU": "Australia",
    "NP": "Nepal",
    "PK": "Pakistan",
    "AE": "United Arab Emirates",
    "BD": "Bangladesh",
    "LK": "Sri Lanka",
    "CN": "China",
    "JP": "Japan",
    "FR": "France",
    "DE": "Germany",
    "IT": "Italy",
    "ES": "Spain",
    "BR": "Brazil",
    "MX": "Mexico",
    "RU": "Russia",
    "KR": "South Korea"
}



def predict_nationality(emp_name):
    try:
        response = requests.get(NATIONALIZE_API_URL,params={"name": emp_name},timeout=5)
        response.raise_for_status()
        data = response.json()
        countries = []

        for country in data.get("country", []):
            code = country["country_id"]
            countries.append(
                {
                    "country_code": code,
                    "country_name": COUNTRY_NAMES.get(code, code),
                    "probability": round(country["probability"] * 100,2)
                }
            )
        return {
            "name": data.get("name"),
            "count": data.get("count"),
            "countries": countries
        }
    
    except requests.exceptions.Timeout:
        return {"error": "Unable to fetch (Request Timed Out)."}

    except requests.exceptions.ConnectionError:
        return {"error": "No Internet Connection."}

    except requests.exceptions.HTTPError:
        return {"error": "Service returned an error."}

    except Exception:
        return {"error": "Nationality Prediction Service unavailable."}
    

