import json
import pandas as pd
from datetime import datetime


voef = open('voe.json', 'r')
voepf = open('voeprev.json', 'r')
localdidf = open('localdidref.json', 'r')

voej = json.load(voef)
voepj = json.load(voepf)
localdj = json.load(localdidf)

voef.close()
voepf.close()
localdidf.close()

df_curr = pd.DataFrame.from_dict(voej)
df_prev = pd.DataFrame.from_dict(voepj)

changes = []

addcount = 0
dropcount = 0
changecount = 0


for index, row in df_curr.iterrows():
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    matching_rows = df_prev[df_prev['DID'] == row['DID']]
    if not matching_rows.empty:
        prev_row = matching_rows.iloc[0]
        if row['IP'] != prev_row['IP']:
            changes.append({
                "Date": date_str,
                "Time": time_str,
                "DID": row['DID'],
                "DP": row['ParentDP'],
                "SiteName": row['Name'],
                "Event": "IP changed"
            })
            changecount += 1
    else:
        changes.append({
            "Date": date_str,
            "Time": time_str,
            "DID": row['DID'],
            "DP": row['ParentDP'],
            "SiteName": row['Name'],
            "Event": "Added"
        })
        addcount += 1


for index, row in df_prev.iterrows():
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    matching_rows = df_curr[df_curr['DID'] == row['DID']]
    if matching_rows.empty:
        changes.append({
            "Date": date_str,
            "Time": time_str,
            "DID": row['DID'],
            "DP": localdj[row['DID']]['ParentDP'],
            "SiteName": row['Name'],
            "Event": "Dropped"
        })
        dropcount += 1

print("\nSites IP changes =", changecount)
print("Sites Dropped =", dropcount)
print("Sites Added =", addcount)
print("Total changes =", addcount + dropcount + changecount)

with open('json_analysis.json', 'w') as outfile:
    json.dump(changes, outfile,indent=2)

