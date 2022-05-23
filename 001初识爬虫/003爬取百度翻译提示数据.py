
# 爬取百度翻译提示数据

import requests

# 定义爬取的网址链接
url = " https://fanyi.baidu.com/sug";

# 输入想要查询的内容
query = input("请输入要翻译的内容：")
req = {
    "kw": query
}

# 调用requests 库发送请求，获取结果
resp = requests.post(url, data=req)

# 使用json()不会产生乱码问题
print(resp.json())

# 关掉请求
resp.close()

