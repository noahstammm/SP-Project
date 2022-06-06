from decimal import Decimal
import json
from typing import List, Any

import pandas as pd

import requests
from dto.football.football_dto import FootballDto

teams_wins = int
teams_lost = int

api_token = "?api_token=sahmC5rxgV1pUEJyQ98314ySQtZ19MyyXhUsTxXOpJsgmoTe0cgWWNKr7H99"


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


def get_team_statistics(teams_name) -> [str]:
    # Request team
    team = teams_name
    url = f"https://soccer.sportmonks.com/api/v2.0/teams/search/{team}?api_token=zLKFDGJ9CvmFi0BvnMBY0psu2g0bhP6KiMS9MRMnvR4ArUzB7Er7v4bKBuQr"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    content = json.loads(response.text)
    print("Team Content: ", content)

    # get the team id and the current season id from the json
    teams_id_list = list(map(lambda season: season.get('id'), content.get('data')))
    team_id = str(teams_id_list)
    start = "["
    end = "]"
    team_id = team_id.split(start)[1].split(end)[0]
    print("Team id: ", team_id)

    current_season_list = list(map(lambda season: season.get('current_season_id'), content.get('data')))
    current_season_id = str(current_season_list)
    start = "["
    end = "]"
    current_season_id = current_season_id.split(start)[1].split(end)[0]
    print("Season id ", current_season_id)

    # Request season
    url_season = f"https://soccer.sportmonks.com/api/v2.0/seasons/{current_season_id}?api_token=zLKFDGJ9CvmFi0BvnMBY0psu2g0bhP6KiMS9MRMnvR4ArUzB7Er7v4bKBuQr"

    payload = {}
    headers = {}

    response_season = requests.request("GET", url_season, headers=headers, data=payload)

    content_season = json.loads(response_season.text)
    current_round_id = content_season['data']['current_round_id']
    print("Round id:", current_round_id)

    # Get current round

    url_round = f"https://soccer.sportmonks.com/api/v2.0/rounds/{current_round_id}?api_token=zLKFDGJ9CvmFi0BvnMBY0psu2g0bhP6KiMS9MRMnvR4ArUzB7Er7v4bKBuQr"

    payload = {}
    headers = {}

    response_round = requests.request("GET", url_round, headers=headers, data=payload)

    content_round = json.loads(response_round.text)
    current_round_id = content_round['data']
    start_date = content_round['data']['start']
    end_date = content_round['data']['end']
    print(start_date, "and", end_date)
    print("This is the current round: ", current_round_id)

    # Get Fixture

    url_fixture = f"https://soccer.sportmonks.com/api/v2.0/fixtures/between/{start_date}/{end_date}/{team_id}?api_token=zLKFDGJ9CvmFi0BvnMBY0psu2g0bhP6KiMS9MRMnvR4ArUzB7Er7v4bKBuQr"

    payload = {}
    headers = {}

    response_fixture = requests.request("GET", url_fixture, headers=headers, data=payload)

    content_fixture = json.loads(response_fixture.text)
    current_fixture_id = content_fixture['data'][0]['id']
    print("This is the current fixture: ", current_fixture_id)

    # Get odds
    url_odds = f"https://soccer.sportmonks.com/api/v2.0/odds/fixture/{current_fixture_id}?api_token=zLKFDGJ9CvmFi0BvnMBY0psu2g0bhP6KiMS9MRMnvR4ArUzB7Er7v4bKBuQr"

    payload = {}
    headers = {}

    response_odds = requests.request("GET", url_odds, headers=headers, data=payload)

    content_odds = json.loads(response_odds.text)
    current_odds_name = content_odds['data'][0]['bookmaker']['data'][0]['name']
    current_odds_probability = content_odds['data'][0]['bookmaker']['data'][0]['odds']['data'][0]['probability']
    print("This is the current odds name: ", current_odds_name)
    print("This is the current odds odds: ", current_odds_probability)

    # Get stats
    url_stat = f"https://soccer.sportmonks.com/api/v2.0/teams/{team_id}?api_token=zLKFDGJ9CvmFi0BvnMBY0psu2g0bhP6KiMS9MRMnvR4ArUzB7Er7v4bKBuQr&include=stats&seasons={current_season_id}"

    payload = {}
    headers = {}

    response_stat = requests.request("GET", url_stat, headers=headers, data=payload)
    content_stat = json.loads(response_stat.text)
    print(content_stat)

    team_wins = content_stat['data']['stats']['data'][0]['win']['total']
    team_lost = content_stat['data']['stats']['data'][0]['lost']['total']

    return current_odds_name, current_odds_probability, team_wins, team_lost


def probability_to_win(wins, lost) -> float:
    total_games = wins + lost
    win_probability = 100 / total_games * wins
    print("Total games played: ", total_games)

    return win_probability


def get_standingsregular():
    url_stands = f"https://soccer.sportmonks.com/api/v2.0/standings/season/18334/{api_token}"

    payload = {}
    headers = {}

    # position = str
    response_stands = requests.request("GET", url_stands, headers=headers, data=payload)
    content_stands = json.loads(response_stands.text)
    length_r = 12
    # length_champ = 6
    # length_relegation = 6
    data = {
        "Position": [],
        "Name": [],
        "Played Games": [],
        "Won": [],
        "Lost": [],
        "Draws": [],
        "+/-": [],
        "Points": []

    }

    i = 0
    while i < length_r:
        data.get("Position").append(content_stands['data'][0]['standings']['data'][i]['position'])
        data.get("Name").append(content_stands['data'][0]['standings']['data'][i]['team_name'])
        data.get("Played Games").append(content_stands['data'][0]['standings']['data'][i]['overall']['games_played'])
        data.get("Won").append(content_stands['data'][0]['standings']['data'][i]['overall']['won'])
        data.get("Lost").append(content_stands['data'][0]['standings']['data'][i]['overall']['lost'])
        data.get("Draws").append(content_stands['data'][0]['standings']['data'][i]['overall']['draw'])
        data.get("+/-").append(((content_stands['data'][0]['standings']['data'][i]['overall']['goals_scored'])
                                - (content_stands['data'][0]['standings']['data'][i]['overall']['goals_against'])))
        data.get("Points").append(content_stands['data'][0]['standings']['data'][i]['overall']['points'])

        i += 1

    df = pd.DataFrame(data)
    return df


def get_standingsch():
    url_stands = f"https://soccer.sportmonks.com/api/v2.0/standings/season/18334/{api_token}"

    payload = {}
    headers = {}

    # position = str
    response_stands = requests.request("GET", url_stands, headers=headers, data=payload)
    content_stands = json.loads(response_stands.text)
    length_r = 6

    datach = {
        "Position": [],
        "Name": [],
        "Played Games": [],
        "Won": [],
        "Lost": [],
        "Draws": [],
        "+/-": [],
        "Points": []

    }

    i = 0
    while i < length_r:
        datach.get("Position").append(content_stands['data'][2]['standings']['data'][i]['position'])
        datach.get("Name").append(content_stands['data'][2]['standings']['data'][i]['team_name'])
        datach.get("Played Games").append(content_stands['data'][2]['standings']['data'][i]['overall']['games_played'])
        datach.get("Won").append(content_stands['data'][2]['standings']['data'][i]['overall']['won'])
        datach.get("Lost").append(content_stands['data'][2]['standings']['data'][i]['overall']['lost'])
        datach.get("Draws").append(content_stands['data'][2]['standings']['data'][i]['overall']['draw'])
        datach.get("+/-").append(((content_stands['data'][2]['standings']['data'][i]['overall']['goals_scored'])
                                  - (content_stands['data'][2]['standings']['data'][i]['overall']['goals_against'])))
        datach.get("Points").append(content_stands['data'][2]['standings']['data'][i]['overall']['points'])

        i += 1

    df = pd.DataFrame(datach)

    return df


def get_standingsrel():
    url_stands = f"https://soccer.sportmonks.com/api/v2.0/standings/season/18334/{api_token}"

    payload = {}
    headers = {}

    response_stands = requests.request("GET", url_stands, headers=headers, data=payload)
    content_stands = json.loads(response_stands.text)
    length_r = 6

    datarel = {
        "Position": [],
        "Name": [],
        "Played Games": [],
        "Won": [],
        "Lost": [],
        "Draws": [],
        "+/-": [],
        "Points": []

    }

    i = 0
    while i < length_r:
        datarel.get("Position").append(content_stands['data'][1]['standings']['data'][i]['position'])
        datarel.get("Name").append(content_stands['data'][1]['standings']['data'][i]['team_name'])
        datarel.get("Played Games").append(content_stands['data'][1]['standings']['data'][i]['overall']['games_played'])
        datarel.get("Won").append(content_stands['data'][1]['standings']['data'][i]['overall']['won'])
        datarel.get("Lost").append(content_stands['data'][1]['standings']['data'][i]['overall']['lost'])
        datarel.get("Draws").append(content_stands['data'][1]['standings']['data'][i]['overall']['draw'])
        datarel.get("+/-").append(((content_stands['data'][1]['standings']['data'][i]['overall']['goals_scored'])
                                   - (content_stands['data'][1]['standings']['data'][i]['overall']['goals_against'])))
        datarel.get("Points").append(content_stands['data'][1]['standings']['data'][i]['overall']['points'])

        i += 1

    df = pd.DataFrame(datarel)

    return df


def get_season_ids():
    url_seasonall = f"https://soccer.sportmonks.com/api/v2.0/seasons{api_token}"

    payload = {}
    headers = {}

    response = requests.request("GET", url_seasonall, headers=headers, data=payload)
    all_seasons = json.loads(response.text)
    length_r = 25

    data = {
        "Season ID": [],
        "Season": [],
        "League ID": [],
        "Current Season": [],
        "Current Round ID": [],
        "Current Stage ID": []
    }

    i = 0
    while i < length_r:
        data.get("Season ID").append(all_seasons['data'][i]['id'])
        data.get("Season").append(all_seasons['data'][i]['name'])
        data.get("League ID").append(all_seasons['data'][i]['league_id'])
        data.get("Current Season").append(all_seasons['data'][i]['is_current_season'])
        data.get("Current Round ID").append(all_seasons['data'][i]['current_round_id'])
        data.get("Current Stage ID").append(all_seasons['data'][i]['current_stage_id'])

        i += 1

    df = pd.DataFrame(data)
    df = df.loc[df['League ID'] == 271]
    return df
