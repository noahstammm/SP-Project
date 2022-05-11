import json
import requests


def main() -> None:
    url = "https://soccer.sportmonks.com/api/v2.0/countries/320/teams?api_token=zLKFDGJ9CvmFi0BvnMBY0psu2g0bhP6KiMS9MRMnvR4ArUzB7Er7v4bKBuQr"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    content = json.loads(response.text)

    print(content.get('data'))

    print('-------------------')
    print(content.get('name'))

    newlist = list(map(lambda team: team.get('name'), content.get('data')))

    print(newlist)


if __name__ == '__main__':
    main()