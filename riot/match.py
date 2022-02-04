# MATCH-V5

import requests
import time


def getmatches(puuid, api_key, retry=True):
    url = 'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/' + puuid + '/ids?queue=420&start=0&count=100'
    req = requests.get(url, headers={'X-Riot-Token': api_key})

    if retry and req.status_code == 429:
        time.sleep(int(req.headers['Retry-After']))
        req = requests.get(url, headers={'X-Riot-Token': api_key})

    return set(req.json())


def getmatch(matchid, api_key, retry=True):
    url = 'https://asia.api.riotgames.com/lol/match/v5/matches/' + matchid
    req = requests.get(url, headers={'X-Riot-Token': api_key})

    if retry and req.status_code == 429:
        time.sleep(int(req.headers['Retry-After']))
        req = requests.get(url, headers={'X-Riot-Token': api_key})

    return req.json()
