from django.shortcuts import render
from django.http import HttpResponse

html = """
<!DOCTYPE html>
<html>
<head>
<title>主页</title>
<style>
    .d1{
        width: 100%;
        height: 100%;
        background-image: url(https://www.hualigs.cn/image/60c08f2169031.jpg);
        background-size: 100%;
    }
    .d2{
        opacity: 1;
        width: 40%;
        height: 30%;
        font-family: Times New Roman;
        font-size: 500%;
        color: white;
        text-align: center;
        position: absolute;
        top: 0;
        bottom: 0;
        right: 0;
        left: 0;
        margin: auto;
    }
</style>
</head>
<body>
</body>
</html>
"""


def index(requests):
    return HttpResponse(html)