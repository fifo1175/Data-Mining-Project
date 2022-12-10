import pandas as pd

data = pd.read_csv('data.csv')

print(data.info())
del data[data.columns[0]]
neigh = set(data['Neighborhood'])
neigh = list(neigh)

print(len(neigh))
for i in neigh:
    print(i)