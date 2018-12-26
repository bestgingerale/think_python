import pandas as pd

data = pd.read_csv('food/foods_hierarchy.csv', usecols=('name_cn', 'level1'))

data = data.iloc[561:5441]

# data.loc[data['name_cn'] == '爆炒土鸭子', 'level1'] = 'duck_dishes'
# print(data[data['name_cn'] == '爆炒土鸭子'])


rules = {
    '鸡汤': 'chicken_soup',
    '鸭汤': 'duck_soup',
    '(?<!羊|牛|鸡)肉': 'pork',
    '包子': 'steamed_bun'
}

for keys, values in rules.items():
    data.loc[data['name_cn'].str.contains(keys, na=False, regex=True), 'level1'] = values

print(data[data['level1'].notna()])

# print(data[data['name_cn'].str.contains('鸭汤', na=False, regex=False)])


data.to_csv('foods-modified.csv', encoding='utf-8')
