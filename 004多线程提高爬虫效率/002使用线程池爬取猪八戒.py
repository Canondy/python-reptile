# 使用线程池爬取猪八戒  爬取网址：https://beijing.zbj.com/search/f/?kw=小程序

import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor


f = open("data/002data.cvs", mode="w", encoding="utf-8")
csv_writer = csv.writer(f)

# 爬取网页源代码并解析
def down_page_html(url, items):
    resp = requests.get(url)
    html = etree.HTML(resp.text)
    all = html.xpath("/html/body/div[6]/div/div/div[3]/div[5]/div[1]/div")
    for item in all:
        # 商家名
        shop_name = item.xpath("./div/div/a[1]/div[1]/p/text()")[1].replace('\n', '')
        # title
        # 获取整块div内的title
        # title = f"小程序".join(item.xpath("./div/div/a[2]/div[2]/div[2]/p/text()"))
        title = f"{items}".join(item.xpath("./div/div/a[2]/div[2]/div[2]/p/text()"))
        res = [shop_name, title]
        csv_writer.writerow(res)

if __name__ == '__main__':
    # url = f"https://beijing.zbj.com/search/f/?kw=小程序"
    # down_page_html(url)

    # 使用线程池爬取
    query = ["小程序", "saas", "公众号", "ios", "app", "安卓"]
    # 创建线程池
    with ThreadPoolExecutor(6) as t:
        for item in query:
            url = f"https://beijing.zbj.com/search/f/?kw={item}"
            for i in range(1, 7):
                t.submit(down_page_html, url, item)

