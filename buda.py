import requests
import json
from datetime import datetime, timedelta
from buda_auth import BudaHMACAuth
from tabulate import tabulate

url = "https://www.buda.com/api/v2"

f = open('config.json')
auth = json.load(f)

api_key = auth["API_KEY"]
secret = auth["SECRET"]

#timestamp for the last 24hours
last24hours = round((datetime.now() - timedelta(hours = 24)).timestamp())
last24h_params = {'last_timestamp': last24hours}

marketsList = (requests.get(url+"/markets", auth=BudaHMACAuth(api_key, secret))).json()

data = []

for markets in marketsList["markets"]:
    print("================================================================")

    marketsId = markets["id"]

    tradesPerMarket = requests.get(url+f"/markets/{marketsId}/trades", params=last24h_params, auth=BudaHMACAuth(api_key, secret)).json()
    entriesPerMarket = tradesPerMarket["trades"]["entries"]

    #get the higher value tx
    listOfValues = []
    for entries in entriesPerMarket:
        higherValueTx = round(float(entries[1])*float(entries[2]), 3)
        listOfValues.append(higherValueTx)

    item = {"marketId": marketsId, "higherTx": max(listOfValues)}
    # item = {"marketId": marketsId, "higherTx": max(listOfValues), "entries": len(entriesPerMarket)}
    print(item)

    data.append(item)
print("================================================================")
print("            HTML TABLE, data rounded by 3 decimals")
print("================================================================")
print(tabulate(data, tablefmt='html', disable_numparse=True))
# jsonData=json.dumps(data)
#
# with open("test.json", "w") as outfile:
#     outfile.write(jsonData)
