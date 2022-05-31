from flask import Flask, render_template, request

from decimal import Decimal
import json
import requests

from django.tests.utils_tests.test_module.another_good_module import content

api_token = str

api_token = "?api_token=sahmC5rxgV1pUEJyQ98314ySQtZ19MyyXhUsTxXOpJsgmoTe0cgWWNKr7H99"

url_season = f"https://soccer.sportmonks.com/api/v2.0/seasons/18334?api_token=zLKFDGJ9CvmFi0BvnMBY0psu2g0bhP6KiMS9MRMnvR4ArUzB7Er7v4bKBuQr"
payload = {}
headers = {}

response_season = requests.request("GET", url_season, headers=headers, data=payload)
content_season = json.loads(response_season.text)
current_round_id = content_season['data']['current_round_id']

print(current_round_id)

url_stands = f"https://soccer.sportmonks.com/api/v2.0/standings/season/18334/{api_token}"

payload = {}
headers = {}

# position = str
response_stands = requests.request("GET", url_stands, headers=headers, data=payload)
content_stands = json.loads(response_stands.text)

print("-------------Regular Season-------------------")
length_r = 12
length_champ = 6
length_relegation = 6

i = 0


class TableRS:
    def __int__(self, position, team, gp, won, lost, draw, plusminus, points):
        self.position = position
        self.team = team
        self.gp = gp
        self.won = won
        self.lost = lost
        self.draw = draw
        self.points = points


while i < length_r:
    rs_pos = content_stands['data'][0]['standings']['data'][i]['position']
    rs_name = content_stands['data'][0]['standings']['data'][i]['team_name']
    rs_playedgames = content_stands['data'][0]['standings']['data'][i]['overall']['games_played']
    rs_won = content_stands['data'][0]['standings']['data'][i]['overall']['won']
    rs_lost = content_stands['data'][0]['standings']['data'][i]['overall']['lost']
    rs_draw = content_stands['data'][0]['standings']['data'][i]['overall']['draw']
    rs_plusminus = ((content_stands['data'][0]['standings']['data'][i]['overall']['goals_scored']) - (
        content_stands['data'][0]['standings']['data'][i]['overall']['goals_against']))
    rs_points = content_stands['data'][0]['standings']['data'][i]['overall']['points']

    print("Pos: " + str(rs_pos) + " Club: " + rs_name + " Games Played: " + str(rs_playedgames) + " Won: " + str(
        rs_won) + " Lost: " + str(rs_lost) + " Draw: " + str(rs_draw) + " +/-: " + str(
        rs_plusminus) + " Points: " + str(rs_points))
    i += 1

print("-------------Relegation-------------------")
for relegation in content_stands['data'][1]['standings']['data']:
    print(relegation)

print("-------------Championship Round-------------------")
for championship in content_stands['data'][1]['standings']['data']:
    print(championship)

# position = (content_stands['data']['standings']['data'][0]['position'])


# print(content_stands)
# print(position)

# current_stands_list = list(map(lambda standings: standings.get('team_name'), content.get('data')))
# team_name = (current_stands_list)
# start = "["
