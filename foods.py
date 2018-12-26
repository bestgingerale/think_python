import pandas as pd
import re

data = pd.read_csv('foods_hierarchy.csv', names=['1', '2', '3', '4',
                                                 '5', '6', '7', '8', '9',
                                                 '10', '11', '12', '13', '14'])
data = data.drop(['1', '2', '3', '4', '7', '8', '9',
                 '10', '11', '12', '13', '14'], axis=1)
data = data.iloc[561:5442]

data = data.rename(columns={'5': 'Dishes', '6': 'Mapping'})

# #
# for n in re.findall(r'\w*\w*\w*\w*蛋糕', str(data.Dishes)):
#     dfb = int(data[data['Dishes'] == n].index[0])   # return the index
#     data.xs(dfb)['Mapping'] = 'cakes'
#     data.loc[dfb, 'Mapping'] = 'cakes'
#     print(dfb, n)
#     # print(data.loc[dfb, ['Dishes', 'Mapping']])


# print(data.Dishes[5441])
# print(data.values[0])

data.to_csv('foods-modified.csv', encoding='utf-8')
