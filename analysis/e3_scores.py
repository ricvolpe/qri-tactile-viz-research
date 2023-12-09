import pandas as pd

data = pd.read_csv('data/e3_emotions.csv')
accuracy = (data['emotion'] == data['depiction']).sum() / len(data)
matrix = pd.crosstab(data['emotion'], data['depiction'], margins=True)

print(accuracy)
print()
print(matrix)
print()

stats_deptict = data.groupby(['depiction'])[['embody', 'valence', 'arousal']].mean().round(2)
print(stats_deptict)
print()

answ_deptict = data.groupby(['emotion'])[['embody', 'valence', 'arousal']].mean().round(2)
print(answ_deptict)
print()

print(data[['embody', 'valence', 'arousal']].corr())