# AFL Stats Pro Table
# Tutorial from John Watson Rooney YouTube channel

# Developer tools > Network > XHR 
# Reload page and look for API
# Right click > copy as cURL
# Postman > Import > Raw text > paste in cURL
# Hit Send > copy Python code into .py file

import requests
import json
import pandas as pd

url = "https://api.afl.com.au/statspro/playersStats/seasons/CD_S2021014"

payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Origin': 'https://www.afl.com.au',
  'Referer': 'https://www.afl.com.au/stats/stats-pro',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
  'x-media-mis-token': '3e89a10c8bda9b0544dd60705ddf9ba4',
  'Cookie': 'JSESSIONID=788D8475397B2D3D3199DBF2C358DDB6'
}

response = requests.get(url, headers=headers, data=payload)

data = response.json()

print(data.keys())
print(data['totalResults'])

df = pd.json_normalize(data['players'])
print(df.head())

df.to_csv('AFL-Stats-Table.csv', index=False)
print('Items saved to CSV file.')
