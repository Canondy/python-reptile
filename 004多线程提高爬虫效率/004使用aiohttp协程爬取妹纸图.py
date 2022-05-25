
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
    # 从url中截取文件名称  从右边切，切一次，拿[1]的内容
    name = url.rsplit("/", 1)[1]
    # 使用aiohttp 发送请求
    async with aiohttp.ClientSession() as session:
        # 请求异步请求 url 得到图片内容
        async with session.get(url) as res:
            # 下载图片   还可以使用 aiofiles 异步下载
            with open("img/" + name, mode="wb") as f:
                # 读取内容是异步操作，用await挂起
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
