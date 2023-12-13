from LoopData import loopData
from datetime import date
import requests as req
from search import fav_match_search

add_apikey = input("Enter your apiKey :")


def callingApi():
    res = req.get(
        f"https://api.cricapi.com/v1/currentMatches?apikey={add_apikey}&offset=0") 
    cricket_data = res.json()
    return cricket_data


today = date.today()
print(f" \n                                                                Date:{today} Cricket Matches       \n                           ")
data = callingApi()
loopData(data)
fav_match_search(data)

if __name__ == "__main__":
    callingApi()
