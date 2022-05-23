
# 导入requests
import requests

# 准备url
url = "https://movie.douban.com/j/search_subjects"

# 请求参数，在requests中会进行----->url地址拼接
paramter = {
    "type": "movie",
    "tag": "喜剧",
    "sort": "recommend",
    "page_limit": 20,
    "page_start": 0
}

# 参数中需要加headers，因为豆瓣网有---反爬---机制，
# 加headers模拟浏览器请求
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
}

# 调用requests。get()爬取数据
resp = requests.get(url=url, params=paramter, headers=header)

# 查看请求的URL地址
print(resp.request.url)
# 查看请求的headers参数，查看目的主要是--绕过反爬机制
print(resp.request.headers)

print(resp.json())

# 关掉请求
resp.close()