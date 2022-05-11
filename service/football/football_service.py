from decimal import Decimal
import json
import requests


def footballService(team: str) -> Decimal:
    # Formel von Laplace
    # https://de.wikipedia.org/wiki/Laplace-Formel
    return 100


def get_teams() -> [str]:
    url = "https://soccer.sportmonks.com/api/v2.0/countries/320/teams?api_token=zLKFDGJ9CvmFi0BvnMBY0psu2g0bhP6KiMS9MRMnvR4ArUzB7Er7v4bKBuQr"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    content = json.loads(response.text)

    teams = list(map(lambda team: team.get('name'), content.get('data')))
    return teams
