import requests
import json
response = requests.get("https://datis.clowd.io/api/KBOS")
atis = json.loads(response.content)
x = input("what runway do you want to look for?")
if x in str(atis):
    print("using " + x)
else:
    print("runway not being used")