
# 安装lxml  pip install lxml

# 导入etree
import requests
from lxml import etree

# 可以解析xml和html

# 使用requests爬取html页面
url = "https://beijing.zbj.com/search/f/?kw=小程序"
result = requests.get(url)
# print(result.text)

# 解析并提取数据
tree = etree.HTML(result.text)
# 获取div整块内容   使用浏览器的F12 复制xpath
divs = tree.xpath("/html/body/div[6]/div/div/div[3]/div[5]/div[1]/div")

# 进一步提取div里面的内容
for allDiv in divs:
    # 获取商家名
    shop = allDiv.xpath("./div/div/a[1]/div[1]/p/text()")[1].replace('\n', '')
    # 商家所在城市
    site = allDiv.xpath("./div/div/a[1]/div[1]/div/span/text()")[0]
    # 服务商星级
    star = allDiv.xpath("./div/div/a[1]/div[2]/span[2]/i[2]/text()")
    if len(star) == 0:
        star = ''
    # 品牌名店
    famousStore = allDiv.xpath("./div/div/a[1]/div[2]/object/a/div/text()")
    if len(famousStore) == 0:
        famousStore = ''
    # 认证
    auth = allDiv.xpath("./div/div/a[1]/div[2]/span[3]/i/text()")
    if len(auth) == 0:
        auth = ''
    # 获取整块div内的价格
    price = allDiv.xpath("./div/div/a[2]/div[2]/div[1]/span[1]/text()")[0].strip("￥")
    # 成交量
    volume = allDiv.xpath("./div/div/a[2]/div[2]/div[1]/span[2]/text()")[0]
    # print(price)
    # 获取整块div内的title
    title = "小程序".join(allDiv.xpath("./div/div/a[2]/div[2]/div[2]/p/text()"))
    # 获取整块div内的标签
    serviceTag = allDiv.xpath("./div/div/a[2]/div[2]/div[3]/span/text()")
    print((shop, site, star, famousStore, auth, price, volume, title, serviceTag))
result.close()