import json

import pandas as pd


with open('voechangetrend.json', 'r') as file:

    data = json.load(file)


df = pd.DataFrame(data)

df.sort_values(by='Date')

df.sort_values(by='Time')

df = df.sort_values(by='SiteName')


dictionary_changed={}

for i in data:
    if i['SiteName'] not in dictionary_changed:
        if i['Event'].startswith('Added'):
            dictionary_changed[i['SiteName']]={'Dropped':0,'Added':1,'Changed':0}
        elif i['Event'].startswith('Dropped'):
            dictionary_changed[i['SiteName']]={'Dropped':1,'Added':0,'Changed':0}
        elif i['Event'].startswith('IP'):
            dictionary_changed[i['SiteName']]={'Dropped':0,'Added':0,'Changed':1}
    else:
        if i['Event'].startswith('Added'):
            dictionary_changed[i['SiteName']]['Added']+=1
        elif i['Event'].startswith('Dropped'):
            dictionary_changed[i['SiteName']]['Dropped']+=1
        elif i['Event'].startswith('IP'):
            dictionary_changed[i['SiteName']]['Changed']+=1

for i in dictionary_changed:
    print(i)
    print(dictionary_changed[i])

sorted_entries = sorted(dictionary_changed.items(), key=lambda x: (x[1]['Added'], x[1]['Dropped'], x[1]['Changed']), reverse=True)

for site, counts in sorted_entries:
    print(f"Site: {site}")
    print(f"  Dropped: {counts['Dropped']}")
    print(f"  Added: {counts['Added']}")
    print(f"  Changed: {counts['Changed']}")

            

        



 