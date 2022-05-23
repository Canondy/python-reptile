
# 需求：获取电影天堂 电影名称 及 下载链接
# 1.爬取网页 2.网页进行解析 3.存入到cvs文件中

# 1.定位到2022必看热片
# 2.从2022必看热片中获取子页面的链接地址
# 3.请求子页面链接地址，获取我们想要的资源

# 这个爬取的速度较慢，不知道什么原因

import requests
import re
import csv

domain = "https://dytt89.com/"
# verify=False 去掉安全验证
urlRes = requests.get(domain, verify=False)
# 解决获取结果乱码问题
urlRes.encoding = 'gb2312'
# print(urlRes.text)

# 预加载正则表达式
# 解析 2022必看热片 ul里面的内容
reg1 = re.compile(r"2022必看热片.*?<ul>(?P<li>.*?)</ul>", re.S)
reg2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
reg3 = re.compile(r'◎片　　名　(?P<name>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf">'
                  r'<a href="(?P<url>.*?)">', re.S)

res = reg1.finditer(urlRes.text)
href_list = []
for it in res:
    # print(it.group("li"))
    li = it.group('li')
    res2 = reg2.finditer(li)
    for it2 in res2:
        # print(it2.group("href"))
        href_list.append(domain + it2.group("href"))

# 创建文件
f = open("data/003data.csv", mode='w')
# 准备写入对象
csvWriter = csv.writer(f)

# print(href_list)
for i in href_list:

    ret = requests.get(i)
    ret.encoding = 'gb2312'
    # print(ret.text)
    result = reg3.search(ret.text)
    dict = result.groupdict()
    csvWriter.writerow(dict.values())

urlRes.close()
