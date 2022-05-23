
# 使用代理（目的防止自己的IP请求过多被封)

import requests

# 设置代理
proxy = {
    # 这个代理IP不可用，自行购买
    "http": "http://202.109.157.61:9000"
}


# 设置爬取的网址
url = "http://www.baidu.com"


# 使用request.get()请求爬取
res = requests.get(url, proxies=proxy, verify=False)

# 处理返回结果乱码问题
res.encoding = "utf-8"

print(res.text)