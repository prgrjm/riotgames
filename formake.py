import pandas

pandas.set_option('display.max_colwidth', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.max_rows', None)
pandas.set_option('display.width', None)

var = False
if var:
    gamedata = pandas.read_csv('gamedata.csv')
    win = gamedata['win']
    newlist = []
    for i in range(35486):
        if win[i * 10]:
            newlist.append(1)
        else:
            newlist.append(0)
        print(i)
    newlist = pandas.Series(newlist)
    newlist.to_csv('tf_win.csv', index=False)

var = False
if var:
    tf_championid = [[0 for _ in range(157)] for _ in range(35486)]
    championid = pandas.read_csv('championid.csv')
    for c in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        for index, value in enumerate(championid[c]):
            tf_championid[index][value] = 1
    pandas.DataFrame(tf_championid).to_csv('tf_championid.csv', index=False)

var = True
if var:
    tf_championid = [[0 for _ in range(314)] for _ in range(35486)]
    championid = pandas.read_csv('championid.csv')
    for c in ('0', '1', '2', '3', '4'):
        for index, value in enumerate(championid[c]):
            tf_championid[index][value] = 1
    for c in ('5', '6', '7', '8', '9'):
        for index, value in enumerate(championid[c]):
            tf_championid[index][value+157] = 1

    pandas.DataFrame(tf_championid).to_csv('tf_championid2.csv', index=False)

