
# 1.拿到主页面的源代码，然后提取子页面的链接地址 href
# 2.通过href拿到子页面的内容，从子页面找到图片的下载地址
# 3.下载图片

import requests
from bs4 import BeautifulSoup

# 要爬取的url
url = "https://umei.cc/meinvtupian/"
# 调用requests.get()方法爬取
parse = requests.get(url)
# 处理中文乱码问题
parse.encoding = "utf-8"
# print(parse.text)

# 使用BeautifulSoup进行解析html文本内容
page = BeautifulSoup(parse.text, "html.parser")

lis = page.find("div", attrs={ "class":"swiper-wrapper after" }).find_all("li")
# print(lis)
for li in lis:
    # print(li.find_next("img").get("data-src"))
    # 获取每一个img里面的图片链接
    imgUrl = li.find_next("img").get("data-src")
    # print(imgUrl)
    # 使用requests.get()方法请求图片地址
    imgRes = requests.get(imgUrl)

    # 为图片创建名字    取imgUrl中的名字
    imgName = imgUrl.split("/")[-1]
    with open("picture/" + imgName, mode="wb") as f:
        # 图片内容写入文件
        f.write(imgRes.content)
    print(imgName+"-->保存成功")
print("全部保存成功")