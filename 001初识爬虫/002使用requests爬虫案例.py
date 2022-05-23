
# 安装requests    pip install requests
import requests

# 输入要查询的参数
query = input("请输入要查询的内容：")

# 要爬取的网址
url = f'http://www.baidu.com/s?wd={query}'

# 使用requests进行爬取内容，并获取结果
resp = requests.get(url,"utf-8")

# 设置请求返回结果乱码问题
resp.encoding = 'utf-8'

print(resp)
print(resp.text)