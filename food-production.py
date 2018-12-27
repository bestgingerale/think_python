import pandas as pd

data = pd.read_csv('food-production.csv', sep='delimiter', error_bad_lines=False, names=['name', 'level'])

# data = data.iloc[560:5441]    #---test
data = data[601:2625]  # ---production

# data.loc[data['name_cn'] == '爆炒土鸭子', 'level1'] = 'duck_dishes'
# print(data[data['name_cn'] == '爆炒土鸭子'])

# print(data)

rules = {
    'jitang': 'chicken_soup',
    'tusi': 'toast',
    'yuebing': 'mooncake',
    '$dangao': 'other_types_of_cakes'

}

for keys, values in rules.items():
    data.loc[data['name'].str.contains(keys, na=False, regex=True), 'level'] = values
    # str.extract.data.loc[data['name_cn'].str.contains(keys, na=False, regex=True), 'level1'] = values

print(data[data['level'].notna()])

# To track progress
done = data[data['level'].notna()].shape[0]
total = data.shape[0]

print(f'Progress bar: {done}/{total}.')
print(f'{round(done / total * 100)}% done. {total - done} more to go.')

# print(data[data['name'].str.contains('鸭汤', na=False, regex=False)])

data.to_csv('food-production-modified.csv', encoding='utf-8')
