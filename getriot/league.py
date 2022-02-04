# LEAGUE-V4

import requests
import pandas




"""
import requests
import time
import pandas
import riot.error


def gethighleague(region, tier, queue, api_key, retry=True):
    if region not in ('br1', 'eun1', 'euw1', 'jp1', 'kr', 'la1', 'la2', 'na1', 'oc1', 'ru', 'tr1'):
        raise riot.error.RegionError

    t_dict = {'c': 'challenger', 'gm': 'grandmaster', 'm': 'master'}
    if tier in t_dict:
        tier = t_dict[tier]
    elif tier in t_dict.values():
        pass
    else:
        raise riot.error.TierError

    q_dict = {'solo': 'RANKED_SOLO_5x5', 'flex': 'RANKED_FLEX_SR'}
    if queue in q_dict:
        queue = q_dict[queue]
    elif queue in q_dict.values():
        pass
    else:
        raise riot.error.QueueError

    url = 'https://' + region + '.api.riotgames.com/lol/league/v4/' + tier + 'leagues/by-queue/' + queue
    req = requests.get(url, headers={'X-Riot-Token': api_key})

    if retry and req.status_code == 429:
        time.sleep(int(req.headers['Retry-After']))
        req = requests.get(url, headers={'X-Riot-Token': api_key})

    df1 = pandas.DataFrame(req.json())
    df2 = dict(df1['entries'])
    df2 = pandas.DataFrame(df2).transpose()
    df3 = pandas.concat([df1, df2], axis=1)
    df3 = df3.drop(['entries'], axis=1)

    return df3

"""
