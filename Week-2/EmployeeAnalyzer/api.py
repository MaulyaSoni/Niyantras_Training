import requests
AGIFY_API_URL = "https://api.agify.io"

def predict_emp_age(emp_name):

    try:
        response = requests.get(AGIFY_API_URL, params={"name": emp_name}, timeout=5)
        response.raise_for_status()

        data = response.json()
        return {
            "name": data.get("name"),
            "age": data.get("age"),
            "count": data.get("count"),
        }
    
    except requests.exceptions.Timeout:
        return ("Unable to fetch today's quote (Request Timed Out).","System")

    except requests.exceptions.ConnectionError:
        return ("No Internet Connection.","System")

    except requests.exceptions.HTTPError:
        return ("Service returned an error.","System")

    except Exception:
        return ("Age Prediction Service unavailable.","System")