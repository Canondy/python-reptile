# 简单爬虫
# 我的第一个爬虫
# 导入相对应解析类库
from urllib.request import urlopen

# 定义要爬取的网址
# url = "http://www.baidu.com"
url = "http://www.taobao.com"

# 调用urlopen方法，返回一个结果
resp = urlopen(url)

# with open(文件名，模式，编码方式) 读写文件的方法
# mode="r" 表示读文件   mode="w" 表示写文件
# encoding="utf-8"  表示编码方式为utf-8
with open("../url/baidu.html", mode="w", encoding="utf-8") as f:
    f.write(resp.read().decode("utf-8"))
