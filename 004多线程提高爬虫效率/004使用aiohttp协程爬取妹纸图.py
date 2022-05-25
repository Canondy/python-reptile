
# 使用aiohttp协程爬取妹子图
# 安装aiohttp   pip install aiohttp

import asyncio
import aiohttp

urls = {
    "https://i1.shaodiyejin.com/uploads/tu/201612/276/c42.jpg",
    "http://i1.shaodiyejin.com/uploads/tu/201610/501/c12.jpg",
    "http://i1.shaodiyejin.com/uploads/tu/201609/619/c16.jpg"
}


# 下载图片
async def down_img(url):
    # 从url中截取文件名称
    name = url.rsplit("/", 1)[1]
    # 使用aiohttp
    async with aiohttp.ClientSession() as session:
        # 请求异步请求 url
        async with session.get(url) as res:
            # 下载图片
            with open("img/" + name, mode="wb") as f:
                f.write(await res.content.read())
    print(name, "下载完成")


# 使用aiohttp方式异步处理
async def main():
    tasks = []
    for url in urls:
        tasks.append(down_img(url))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
