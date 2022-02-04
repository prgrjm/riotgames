import pandas

pandas.set_option('display.max_colwidth', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.max_rows', None)
pandas.set_option('display.width', None)

alpha = pandas.read_csv('gamedata.csv')
beta = alpha['championId']

num_dic = dict(zip(set(beta), [i for i in range(157)]))
print(num_dic)
numan = pandas.read_csv('numanswer.csv')


def num_return(n):
    return num_dic[n]


var = False
if var:
    num_list = beta[354850:]
    num_list2 = list(map(num_return, num_list))
    num_pd = pandas.Series(num_list2)
    numanswer = pandas.concat([numan, num_pd], axis=1, ignore_index=True)
    numanswer.transpose().to_csv('championid.csv', index=False)

var = False
if var:
    for index in range(35485):
        num_list = beta[(index * 10):(index * 10 + 10)]
        num_list2 = list(map(num_return, num_list))
        num_pd = pandas.Series(num_list2)
        try:
            num_answer = pandas.concat([num_answer, num_pd], axis=1, ignore_index=True)
        except NameError:
            num_answer = num_pd
        if not index % 100:
            num_answer.to_csv('numanswer.csv', index=False)
            print('saved', index)
    num_answer.to_csv('numanswer.csv', index=False)
    print('complete')
