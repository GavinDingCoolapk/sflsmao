import requests

r = requests.get("https://data.121.com.cn/szmbdata/open/openData.do?type=12&appid=%221621936919915%22&appKey=%22f7ebe38a-b187-4ed7-badc-3d3a4570e8a3%22&parameter=G3567")
r = r.json()['data'][0]
l = list(r.values())
 
h = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>实时天气</title>
</head>

<body>
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
</body>
</html>
""".format(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7])