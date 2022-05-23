
# bs4 官方网址：https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
# 安装 beautifulsoup4    pip install bs4

# 导入requests解析包
# 导入提取包 BeautifulSoup
# 导入csv包
import requests
from bs4 import BeautifulSoup
import csv

url = "https://dytt89.com/"

# verify=False 去掉安全验证
result = requests.get(url, verify=False)
result.encoding = 'gb2312'
# print(result.text)

# 准备写入的文件
f = open("data/004data.csv", mode='w')
csvWriter = csv.writer(f)

# 使用BeautifulSoup解析爬取结果
page = BeautifulSoup(result.text, "html.parser")

# 获取指定style样式的div, 并取所有的li标签
lis = page.find("div", attrs={"style": "float:left;width:470px;height:auto;overflow:hidden;"}).find_all("li")
# print(lis)
for li in lis:
    # 获取li里面a标签的内容 名称
    a = li.find_next("a")
    # 获取li里面span标签的内容  日期
    span = li.find_next("span")
    # print([a.text, span.text])
    csvWriter.writerow([a.text, span.text])

f.close()