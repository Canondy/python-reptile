
# 爬取91看剧视频
# 这个操作会造成PyCharm卡死，谨慎操作

import requests
from lxml import etree

# url = "http://www.wwmulu.com/rj/nsdfz/play-1-1.html"
# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
# }

# regex = re.compile(r'<div class="main">.*?<span class="ff-player" data-play-name="kbm3u8" data-src="(?P<url>.*?)">', re.S)


# res = requests.get(url, headers=header)
# res.encoding = "utf-8"
# html = etree.HTML(res.text)
# # 拿到下载m3u8文件下载地址
# result = html.xpath("/html/body/div[2]/div/div[2]/div/div[2]/span[1]/@data-src")[0]
# # print(result) #https://sod.bunediy.com/20220509/IVBe7rEq/index.m3u8
# res.close()

# 下载m3u8文件
# sec_key = requests.get(result, headers=header)
# with open("data/006data.m3u8", mode="wb") as f:
#     f.write(sec_key.content)

# 读取m3u8文件
n = 1
with open("data/006data.m3u8", mode="r", encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line.startswith("#"):
            continue

        res3 = requests.get(line)
        f = open(f"data/{n}.ts", mode="wb")
        f.write(res3.content)
        f.close()
        res3.close()
        n += 1



