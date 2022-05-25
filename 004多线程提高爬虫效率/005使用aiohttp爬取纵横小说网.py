# 爬取纵横中文网小说  http://www.zongheng.com/
# 爬取的小说 大荒剑帝(随便找的，任何小说都可以)     爬取地址：http://book.zongheng.com/showchapter/1198878.html
# 安装aiofiles     pip install aiofiles

import requests
import aiohttp
import asyncio
import aiofiles
from lxml import etree


# 请求详情页，并下载小说内容
async def down_content(name, href):
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(href, headers=header) as res:
            # 结果前面必须 await   这是一个坑
            # await res.text() 获取html代码
            # await res.json() 获取json格式的响应内容, 返回的是字典
            # print(await res.text())
            result = etree.HTML(await res.text())
            # result.xpath("/html/body/div[2]/div[3]/div[3]/div/div[1]/div[5]")
            # 获取div里面的内容（小说内容）
            content = result.xpath("/html/body/div[2]/div[3]/div[3]/div/div[1]/div[5]/p/text()")
            # name = result.xpath("/html/body/div[2]/div[3]/div[3]/div/div[1]/div[2]/div[2]/text()")[0]
            async with aiofiles.open("data/" + name, mode="w", encoding="utf-8") as f:
                for cont in content:
                    await f.write(cont + "\n")


# 第一次请求获取 网页源代码，解析获得小说章节和章节url，提交给asyncio去异步执行
async def down_html(url):
    # 这一次请求是获取章节 及其 章节url
    resp = requests.get(url)
    tasks = []
    res = etree.HTML(resp.text)
    uls_list = res.xpath("/html/body/div[3]/div[2]/div[2]/div[2]/ul/li")
    for uls in uls_list:
        name = uls.xpath("./a/text()")[0]
        # 取a标签里面的href值（每章小说的url链接）
        href = uls.xpath("./a/@href")[0]
        tasks.append(down_content(name, href))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    url = "http://book.zongheng.com/showchapter/1198878.html"
    asyncio.run(down_html(url))

    # 测试小说每章    内容   下载 逻辑
    # url = "http://book.zongheng.com/chapter/1198878/68077807.html"
    # res = requests.get(url)
    # result = etree.HTML(res)
    # print(result)
    # name = result.xpath("/html/body/div[2]/div[3]/div[3]/div/div[1]/div[2]/div[2]/text()")[0]
    # content = result.xpath("/html/body/div[2]/div[3]/div[3]/div/div[1]/div[5]/p/text()")
    # f = open("data/" + name, mode="w")
    # for cont in content:
    #     f.write(cont + "\n")
