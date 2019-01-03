# fid,name,name_en,name_he,name_cn,level1,level2,level3,level4,level5,level6,level7,level8,level9
# 8017,4cunjiagaoqifengdangao,,,4寸加高戚风蛋糕,,,4cunjiagaoqifengdangao,,,,,,

import numpy as np
import pandas as pd

data = pd.read_csv('food-test.csv', usecols=('name_cn', 'level1'))

data = data.iloc[560:5441]  # ------test
# data = data[601:2625]  # ---production

# data.loc[data['name_cn'] == '爆炒土鸭子', 'level1'] = 'duck_dishes'
# print(data[data['name_cn'] == '爆炒土鸭子'])


rules1 = {
    '鸡汤': 'chicken_soup',
    '鸭汤': 'duck_soup',
    r'((?<!羊|牛|鸡)肉)|炒肉': 'stir_fried_pork',
    '包子': 'steamed_bun',
    '奶茶': 'milk_tea',
    '蛋糕': 'chinese_cakes',
    '吐司': 'toast',
    '龟苓膏': 'guilinggao'
}

rules2 = [
    ('豆', 'chinese_peas'),
    ('土豆', 'chinese_potato_dishes'),
    ('鸡', 'chinese_chicken_dishes'),
    ('饭', 'chinese_mi'),
    ('汤', 'chinese_soup'),
    ('鸡汤', 'chicken_soup'),
    ('鸭汤', 'duck_soup'),
    ('((?<!羊|牛|鸡)肉)|炒肉', 'stir_fried_pork'),
    ('奶茶', 'milk_tea'),
    ('蛋糕', 'chinese_cakes'),
    ('吐司', 'toast'),
    ('龟苓膏', 'guilinggao'),
    ('饺子', 'jiaozi'),
    ('虾', 'chinese_shrimp'),
    ('饺子', 'jiaozi'),
    ('牛奶', 'chinese_milk'),
    ('面', 'chinese_noodles'),
    ('包子', 'steamed_bun'),
    ('面包', 'chinese_bread'),
    ('炒鸡蛋', 'chinese_fried_eggs'),
    ('河粉', 'hefen'),
    ('米线', 'mixian'),
    ('米粉', 'rice_vermicelli')
]


def mapping():
    # for keys, values in rules1.items(): # rules1 list
    for keys, values in rules2:  # rules2 tuple
        data.loc[data['name_cn'].str.contains(keys, na=False, regex=True), 'level1'] = values
        # str.extract.data.loc[data['name_cn'].str.contains(keys, na=False, regex=True), 'level1'] = values
    print(data[data['level1'].notna()])


def progress():  # To track progress
    done = data[data['level1'].notna()].shape[0]
    total = data.shape[0]

    print(f'Progress bar: {done}/{total}.')
    print(f'{round(done / total * 100)}% done. {total - done} more to go.')


def check(v):  # To check specific items
    print(data[data['name_cn'].str.contains(v, na=False, regex=False)])


mapping()
check('铜锣烧')
progress()

data.to_csv('food-test-modified.csv')
# result.to_csv('food-test-left.csv', encoding='utf-8')
