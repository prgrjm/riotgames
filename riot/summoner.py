# SUMMONER-V4

import requests
import time
import pandas
import riot.error


def getsummoner_summonerid(region, summonerid, api_key, retry=True):
    if region not in ('br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ru', 'tr1'):
        raise riot.error.RegionError

    url = 'https://' + region + '.api.riotgames.com/lol/summoner/v4/summoners/' + summonerid
    req = requests.get(url, headers={'X-Riot-Token': api_key})

    if retry and req.status_code == 429:
        time.sleep(int(req.headers['Retry-After']))
        req = requests.get(url, headers={'X-Riot-Token': api_key})

    s1 = pandas.Series(req.json())

    return s1
