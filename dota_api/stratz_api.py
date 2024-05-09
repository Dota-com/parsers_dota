import requests


a = requests.get("https://docs.stratz.com/api/v1/Player/327662605",
                 headers={
                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                                   "Chrome/122.0.0.0 "
                                   "Safari/537.36 "
                                   "Edg/122.0.0.0"}).json()

print(a)