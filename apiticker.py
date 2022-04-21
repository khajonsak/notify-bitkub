import time
import requests
API_HOST = 'https://api.bitkub.com'

url = 'https://notify-api.line.me/api/notify'
token = 'DJ1A6Zlk2AtvUFAfnw1PSkTnnpeFUc2dyPgDT7o22Jl'#token line notify
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
response = requests.get(API_HOST + '/api/market/ticker')
price = response.json()
cion = ["THB_BTC", "THB_ETH", "THB_ADA", "THB_DOGE", "THB_KUB", "THB_SIX", "THB_JFIN", "THB_GALA","THB_SAND"]
i = 0
while i <= 10:
    for c in cion  : 
        sym = c
        data = price[sym]
        lastprice = data["last"]
        msg = sym,  lastprice,
        r = requests.post(url, headers=headers, data = {'message':msg})
        #print (r.text)
    time.sleep(30*60)# set time(second)


