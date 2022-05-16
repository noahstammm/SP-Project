import json
import requests


def main() -> None:

    team_wins= int
    team_lost= int


    def get_team_statistics(teams_name) -> [str]:
        # Request team
        team = teams_name
        url = f"https://soccer.sportmonks.com/api/v2.0/teams/search/{team}?api_token=zLKFDGJ9CvmFi0BvnMBY0psu2g0bhP6KiMS9MRMnvR4ArUzB7Er7v4bKBuQr"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        content = json.loads(response.text)
        print("Team Content: ",content)

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
        print(start_date, "and" , end_date)
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
        print(team_lost)


        total_games = team_wins + team_lost
        print("Total games played: ", total_games)


        return current_odds_name, current_odds_probability

    name = "Horsens"
    get_team_statistics(name)




if __name__ == '__main__':
    main()

