from flask import Flask, render_template, request

from decimal import Decimal
import json
import requests



api_token= str

api_token= "sahmC5rxgV1pUEJyQ98314ySQtZ19MyyXhUsTxXOpJsgmoTe0cgWWNKr7H99"

url_season = f"https://soccer.sportmonks.com/api/v2.0/seasons/18334?api_token=zLKFDGJ9CvmFi0BvnMBY0psu2g0bhP6KiMS9MRMnvR4ArUzB7Er7v4bKBuQr"
payload = {}
headers = {}

response_season = requests.request("GET", url_season, headers=headers, data=payload)
content_season = json.loads(response_season.text)
current_round_id = content_season['data']['current_round_id']




url_standings = f"https://soccer.sportmonks.com/api/v2.0/standings/season/18334/round/{current_round_id}?api_token=zLKFDGJ9CvmFi0BvnMBY0psu2g0bhP6KiMS9MRMnvR4ArUzB7Er7v4bKBuQr"

payload = {}
headers = {}

response_standings = requests.request("GET", url_standings, headers=headers, data=payload)
content_standings = json.loads(response_standings.text)

print(content_standings)