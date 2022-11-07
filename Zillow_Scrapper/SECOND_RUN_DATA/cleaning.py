import pandas as pd

data = pd.read_csv('house_og.csv')

print(data.info())
del data[data.columns[0]]
data = data.drop_duplicates()
print(data.info())
data.to_csv('./house_og.csv')