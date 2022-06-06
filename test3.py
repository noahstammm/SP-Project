import json

import requests

api_token = "?api_token=sahmC5rxgV1pUEJyQ98314ySQtZ19MyyXhUsTxXOpJsgmoTe0cgWWNKr7H99"


def get_season_ids():
    url_seasonall = f"https://soccer.sportmonks.com/api/v2.0/seasons{api_token}"

    payload = {}
    headers = {}

    response = requests.request("GET", url_seasonall, headers=headers, data=payload)
    all_seasons = json.loads(response.text)

    print(all_seasons)
