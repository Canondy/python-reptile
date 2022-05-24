
# 1.使用requests爬取汽车之家口碑网页源代码
# 2.使用pyquery解析并提取数据

import requests
from pyquery import PyQuery

# 1.提取汽车之家网页源代码
def page_html(url):
    res = requests.get(url)
    res.encoding = "gb2312"
    return res.text

# 2.解析源代码并解析，提取数据
def parse_page_html(html):
    p = PyQuery(html)
    # class = ".mt-10"
    all_list = p(".mt-10").items()
    for list_one in all_list:
        # 处理经销商不存在，而产生数据出现错误的问题, 添加经销商，让数据格式进行统一，以便提取
        shop = list_one("div > dl:nth-child(3) > dt:contains(购车经销商)")
        # 先判断是否存在
        if not shop:
            # 不存在，需要在 购买地点下面添加
            list_one("div > dl:nth-child(2)").after(PyQuery("""
                <dl class="choose-dl">
                        <dt>购车经销商</dt>
                        <dd>
                            <a href="https://dealer.autohome.com.cn/83653#pvareaid=102556" class="js-dearname" data-val="83653,51935" data-evalid="4254510" target="_blank">潍坊广宇奥迪</a>
                        </dd>
                    </dl>
            """))

        # 获取汽车型号
        # div > dl:nth-child(1)  取div里面的第一个dl
        # .eq(0) 筛选结果取第一个  （因为结果里面有不需要的数据）
        car_name = list_one("div > dl:nth-child(1) > dd").eq(0).text().replace("\n", "").replace(" ", "")
        # 获取购买地点
        site = list_one("div > dl:nth-child(2) > dd").text()
        # 获取购买时间
        time = list_one("div > dl:nth-child(4) > dd").text()
        # 获取购车价格
        price = list_one("div > dl:nth-child(5) > dd").text().replace(" 万元", "")
        # 获取油耗
        oil = list_one("div > dl:nth-child(6) > dd > p:nth-child(1)").text().replace(" 升/百公里", " ").replace("\n", "")
        # 行驶公里数
        km = list_one("div > dl:nth-child(6) > dd > p:nth-child(2)").text().replace("公里", "")
        # 其他
        other = list_one("div > div > dl > dd").text().split()
        # print(car_name, site, time, price, oil, other)
        print(oil, km)

if __name__ == '__main__':
    # 需要爬取的网址
    url = "https://k.autohome.com.cn/692/#pvareaid=2099126"
    # 1.提取汽车之家口碑网页源代码
    html = page_html(url)
    # 2.解析源代码并解析，提取数据
    parse_page_html(html)

