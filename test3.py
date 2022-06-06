import json

import pandas as pd

import requests

api_token = "?api_token=sahmC5rxgV1pUEJyQ98314ySQtZ19MyyXhUsTxXOpJsgmoTe0cgWWNKr7H99"


def get_standings():
    url_stands = f"https://soccer.sportmonks.com/api/v2.0/standings/season/18334/{api_token}"

    payload = {}
    headers = {}

    response_stands = requests.request("GET", url_stands, headers=headers, data=payload)
    content_stands = json.loads(response_stands.text)

    print("-------------Regular Season-------------------")
    length_r = 12

    data = {
        "position": [],
        "name": [],
        "Played Games": [],
        "Won": [],
        "Lost": [],
        "Draws": [],
        "+/-": [],
        "Points": []

    }

    i = 0
    while i < length_r:
        data.get("position").append(content_stands['data'][0]['standings']['data'][i]['position'])
        data.get("name").append(content_stands['data'][0]['standings']['data'][i]['team_name'])
        data.get("Played Games").append(content_stands['data'][0]['standings']['data'][i]['overall']['games_played'])
        data.get("Won").append(content_stands['data'][0]['standings']['data'][i]['overall']['won'])
        data.get("Lost").append(content_stands['data'][0]['standings']['data'][i]['overall']['lost'])
        data.get("Draws").append(content_stands['data'][0]['standings']['data'][i]['overall']['draw'])
        data.get("+/-").append(((content_stands['data'][0]['standings']['data'][i]['overall']['goals_scored'])
                                - (content_stands['data'][0]['standings']['data'][i]['overall']['goals_against'])))
        data.get("Points").append(content_stands['data'][0]['standings']['data'][i]['overall']['points'])

    i += 1

    df = pd.DataFrame(data)
    print(df)
