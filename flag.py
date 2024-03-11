import requests

URL = "http://host3.dreamhack.games:18303/api/memo"

headers = {
    'API-KEY': ''
}

res = requests.get(URL, headers=headers)

print(res.text)