from df2gspread import df2gspread as d2g
import os
import pandas as pd
import json

os.remove('newquotes.json')
os.remove('quotes.json')
os.system('scrapy crawl quotes -o quotes.json')

with open('quotes.json', 'r+', encoding='utf8') as f:
    data = json.load(f)
    for element in data:
        jsonfile = element["teste"]
with open('newquotes.json', 'w') as f:
    json.dump(jsonfile, f)
with open('newquotes.json', 'r+', encoding='utf8') as f:
    dataf = json.load(f)
df = pd.read_json(dataf)

# df.to_excel("mdr.xlsx", index=False)

spreadsheet = 'mdr'

wks_name = 'Sheet1'

d2g.upload(df, spreadsheet, wks_name)
