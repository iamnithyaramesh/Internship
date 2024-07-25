import json
import pandas as pd

with open('json_analysis.json', 'r') as file:
    data = json.load(file)


df = pd.DataFrame(data)

df.sort_values(by='Date')
df.sort_values(by='Time')

df.sort_values(by='SiteName')

print(df)


