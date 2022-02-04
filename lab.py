import riot
import pandas

pandas.set_option('display.max_colwidth', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.max_rows', None)
pandas.set_option('display.width', None)

api_key = 'RGAPI-56dfd9f2-47db-43f1-bdc6-35f33238bdef'


var = False
if var:
    cl = riot.gethighleague('kr', 'c', 'solo', api_key)
    gml = riot.gethighleague('kr', 'gm', 'solo', api_key)
    ml = riot.gethighleague('kr', 'm', 'solo', api_key)
    hl = pandas.concat([cl, gml, ml], ignore_index=True)
    hl.to_csv('highleague.csv', index=False)

var = False
if var:
    hl = pandas.read_csv('highleague.csv')

    si = hl['summonerId'][0]
    s1 = riot.getsummoner_summonerid('kr', si, api_key)
    print(s1)
    summonerid = s1

    for si in hl['summonerId'][1:]:
        s1 = riot.getsummoner_summonerid('kr', si, api_key)
        print(s1)
        summonerid = pandas.concat([summonerid, s1], axis=1, ignore_index=True)

    summonerid = summonerid.transpose()
    summonerid.to_csv('summonerid.csv', index=False)

var = False
if var:
    hl = pandas.read_csv('highleague.csv')
    si = pandas.read_csv('summonerid.csv')
    pandas.concat([hl, si], axis=1).to_csv('highlist.csv', index=False)

var = False
if var:
    hl = pandas.read_csv('highlist.csv')
    hl = hl.drop(['id'], axis=1)
    hl.to_csv('highlist.csv', index=False)

var = False
if var:
    hl = pandas.read_csv('highlist.csv')

    pi = hl['puuid'][0]
    s1 = riot.getmatches(pi, api_key)
    matches = s1
    print(len(matches))

    for pi in hl['puuid'][1:]:
        s1 = riot.getmatches(pi, api_key)
        matches = matches | s1
        print(len(matches))
    matches = pandas.Series(tuple(matches))
    matches.to_csv('matches.csv', index=False)

var = False
if var:
    matches = pandas.read_csv('matches.csv')
    mi = matches['matchlist'][0]
    df1 = riot.getmatch(mi, api_key)
    df2 = pandas.DataFrame(df1)['info']['participants']
    df3 = pandas.DataFrame(df2)[['championId', 'championName', 'teamId', 'win']]
    gamedata = df3
    print(0, mi)

    for index, mi in enumerate(matches['matchlist'][1:]):
        df1 = riot.getmatch(mi, api_key)
        df2 = pandas.DataFrame(df1)['info']['participants']
        df3 = pandas.DataFrame(df2)[['championId', 'championName', 'teamId', 'win']]
        gamedata = pandas.concat([gamedata, df3])
        print(index + 1, mi)
        if not index % 100:
            gamedata.to_csv('gamedata.csv')
            print('gamedata saved')

    gamedata.to_csv('gamedata.csv')

var = False
if var:
    matches = pandas.read_csv('matches.csv')
    gamedata = pandas.read_csv('gamedata.csv', index_col=0)

    for index, mi in enumerate(matches['matchlist'][12806:]):
        df1 = riot.getmatch(mi, api_key)
        df2 = pandas.DataFrame(df1)['info']['participants']
        df3 = pandas.DataFrame(df2)[['championId', 'championName', 'teamId', 'win']]
        gamedata = pandas.concat([gamedata, df3])
        print(index + 12806, mi)
        if not index % 100:
            gamedata.to_csv('gamedata.csv')
            print('gamedata saved')

    gamedata.to_csv('gamedata.csv')
