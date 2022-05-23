
# 爬取网页源代码  使用requests
# 解析网页源代码  使用re
# 把解析的内容写入csv中  使用csv

# 导入资源
import requests
import re
import csv

# 准备爬取网址url
url = "https://movie.douban.com/top250"
# 加headers模拟浏览器请求
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
}

result = requests.get(url=url, headers=header)
# print(result.text) 查看爬取的源代码
page_content = result.text

# 预编译正则表达式
regex = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
                   r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                   r'<span>(?P<num>.*?)人评价</span>',re.S)

# 获取解析结果
res = regex.finditer(page_content)

# 创建文件
f = open("data/002data.csv",mode="w")
# 准备csv写入对象
csvWrite = csv.writer(f)

for it in res:
    # print(it.group("name"))
    # print(it.group("year").strip())
    # print(it.group("score"))
    # print(it.group("num"))
    # 将iter转换成字典
    dict = it.groupdict()
    dict['year'] = dict['year'].strip()
    # 将每次获取的值 写入 csv文件中
    csvWrite.writerow(dict.values())