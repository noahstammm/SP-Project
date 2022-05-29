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
position = str
response_stands = requests.request("GET", url_stands, headers=headers, data=payload)
content_stands = json.loads(response_stands.text)
position = (content_stands['data']['standings']['data'][0]['position'])
# print(content_stands)
print(position)

current_stands_list = list(map(lambda standings: standings.get('team_name'), content.get('data')))
team_name = str(current_stands_list)
start="["
