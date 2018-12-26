import pandas as pd

data = pd.DataFrame.from_dict({'A': [1, 2, 3], 'B': [3, 4, 5], 'C': [6, 7, 8]})

data[0] = '?'
data[0:1] = '!'

data2 = pd.DataFrame.from_dict({'AA': [1, 2, 3], 'BB': [3, 4, 5], 'CC': [6, 7, 8]}, 'index')

print(data, end='\n\n')
print(data2)
