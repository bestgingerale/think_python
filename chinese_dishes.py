import pandas as pd
import re

df = pd.read_csv('chinese_dishes_unsorted.csv', names=['dishes', 'mapping'])

p = re.compile('蛋糕', re.UNICODE)

sample = '''4寸加高戚风蛋糕
6寸可可蛋糕
爱心煎饭
爱心小熊便当
Amba酱料
鹌鹑蛋炖猪蹄
鹌鹑豆沙螺丝酥
安庆炒米
腌蒜薹
腌糖醋洋姜
奥尔良板烧鸡腿堡
奥尔良鸡腿堡'''

df['mapping'] = 0.02

# for i in re.findall(r'\w*\w*鸡\w*', str(df.dishes)):
#     print(i)
    # df.set_value(i.index, 'CAT', i)

# print(df.head())
# print(df[['dishes']].head())
# print(df.tail())

# print(df.sample(2))
# print(df[['dishes', 'mapping']])

df.to_csv('chinese_dishes_modified.csv', encoding='utf-8')
