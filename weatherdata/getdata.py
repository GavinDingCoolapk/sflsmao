import requests
import json

r = requests.get("https://data.121.com.cn/szmbdata/open/openData.do?type=12&appid=%221621936919915%22&appKey=%22f7ebe38a-b187-4ed7-badc-3d3a4570e8a3%22&parameter=G3567")
d = r.json()['data'][0]
j = json.dumps(d)
