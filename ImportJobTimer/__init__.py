import datetime
import logging
import requests
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
    logging.info(f"Timer trigger function ran at {utc_timestamp}")

    url = "https://gdm-webappprod.azurewebsites.net/import"

    json_body = {}

    try:
        response = requests.post(url, json=json_body, timeout=30)
        logging.info(f"Called {url} - Status code: {response.status_code}")
        logging.info(f"Response text: {response.text}")
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error calling {url}: {e}")
