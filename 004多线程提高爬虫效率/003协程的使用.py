# 协程的使用，多线程异步执行（io操作，requests网络请求，都会出现线程阻塞）

import time
import asyncio


# 使用协程爬取数据模板
async def test(url):
    print("开始下载")
    # await asyncio.sleep(2)  # 网络请求  使用aiohttp
    print("下载完成")


async def main():
    url = [
        "http://www.baidu.com",
        "http://www.taobao.com",
        "http://www.sougou.com",
    ]

    tasks = []
    for i in url:
        res = test(i)
        tasks.append(res)

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())


# 推荐使用这种方法
# async def test1():
#     print("test1")
#     await asyncio.sleep(3)
#     print("test1")
#
#
# async def test2():
#     print("test2")
#     await asyncio.sleep(3)
#     print("test2")
#
#
# async def test3():
#     print("test3")
#     await asyncio.sleep(3)
#     print("test3")
#
#
# async def main():
#     t1 = test1()
#     t2 = test2()
#     t3 = test3()
#     tasks = [t1, t2, t3]
#     start = time.time()
#     await asyncio.wait(tasks)
#     end = time.time()
#     print(end - start) # 3秒左右
#
# if __name__ == '__main__':
#     asyncio.run(main())


# 1.这种情况，线程等待状态，不能很好利用资源，效率低下
# def test1():
#     print("test1")
#     time.sleep(3)
#     print("test1")
#
#
# def test2():
#     print("test2")
#     time.sleep(3)
#     print("test2")
#
#
# def test3():
#     print("test3")
#     time.sleep(3)
#     print("test3")
#
#
# if __name__ == '__main__':
#     start = time.time()
#     test1()
#     test2()
#     test3()
#     end = time.time()
#     print(end - start)  执行9.01秒  因为睡了9秒  实际执行只用了0.01秒


# 2.效率提升
# async def test1():
#     print("test1")
#     time.sleep(3)
#     print("test1")
#
#
# async def test2():
#     print("test2")
#     time.sleep(3)
#     print("test2")
#
#
# async def test3():
#     print("test3")
#     time.sleep(3)
#     print("test3")
#
#
# if __name__ == '__main__':
#     start = time.time()
#     test1()
#     test2()
#     test3()
#     end = time.time()
#     print(end - start)   # 会报RuntimeWarning警告信息   用了0.006秒


# 3.时间最短
# async def test1():
#     print("test1")
#     await asyncio.sleep(3)
#     print("test1")
#
#
# async def test2():
#     print("test2")
#     await asyncio.sleep(3)
#     print("test2")
#
#
# async def test3():
#     print("test3")
#     await asyncio.sleep(3)
#     print("test3")
#
#
# if __name__ == '__main__':
#     start = time.time()
#     test1()
#     test2()
#     test3()
#     end = time.time()
#     print(end - start)   # 会报RuntimeWarning警告信息   用了0.002-0.004秒




# 4.使用asyncio启动
# async def test1():
#     print("test1")
#     await asyncio.sleep(3)
#     print("test1")
#
#
# async def test2():
#     print("test2")
#     await asyncio.sleep(3)
#     print("test2")
#
#
# async def test3():
#     print("test3")
#     await asyncio.sleep(3)
#     print("test3")
#
#
# if __name__ == '__main__':
#     t1 = test1()
#     t2 = test2()
#     t3 = test3()
#     task = [t1, t2, t3]
#     start = time.time()
#     asyncio.run(asyncio.wait(task))
#     end = time.time()
#     print(end - start)   # 会报RuntimeWarning警告信息   用了3秒


