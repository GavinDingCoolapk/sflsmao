import requests

# r = requests.get("https://data.121.com.cn/szmbdata/open/openData.do?type=12&appid=%221621936919915%22&appKey=%22f7ebe38a-b187-4ed7-badc-3d3a4570e8a3%22&parameter=G3567")
# r = r.json()['data'][0]
# l = r.values()

l = ['2021-06-01 18:00', '26.5', '1001.3', '97', '10.821', '1.1', '1.6', '东南']
 
h = """
<h1>最新天气数据（整点）</h1>
<table border = "1">
    <tr>
        <th>时间</th>
        <th>温度</th>
        <th>气压</th>
        <th>湿度</th>
        <th>能见度</th>
        <th>降雨量</th>
        <th>风速</th>
        <th>风向</th>
    </tr>
    <tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
    </tr>
</table>
""".format(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7])