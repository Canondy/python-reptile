# 导入多线程
from threading import Thread
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# 多线程，多进程，线程池，进程池的使用

# 多线程简单使用
# 1.在一个里面，简单的程序可以使用 不加参数
# def test():
#     for i in range(20):
#         print("test", i)
#
#
# if __name__ == '__main__':
#     # 创建线程并给线程安排任务
#     t = Thread(target=test)
#     # 多线程状态为可以工作状态，具体时间由cpu决定
#     t.start()
#     for i in range(20):
#         print("main", i)

# 2.在一个里面，简单的程序可以使用 不加参数
# def test(name):
#     for i in range(20):
#         print(name, i)
#
#
# if __name__ == '__main__':
#     # 创建线程并给线程安排任务
#     # 参数必须是元组，后边必须加 ,
#     t1 = Thread(target=test, args=("test",))
#     # 多线程状态为可以工作状态，具体时间由cpu决定
#     t1.start()
#     # 创建线程并给线程安排任务
#     t2 = Thread(target=test, args=("thead",))
#     # 多线程状态为可以工作状态，具体时间由cpu决定
#     t2.start()


# 3.复杂的程序使用多线程
# class MyThread(Thread):
#     def run(self):
#         for i in range(20):
#             print("子程序", i)
#
#
# if __name__ == '__main__':
#     t = MyThread()
#     # 开启线程
#     t.start()
#     for i in range(20):
#         print("主线程", i)


# 4.多进程
# def func():
#     for i in range(200):
#         print("func", i)
#
# def t2():
#     for i in range(200):
#         print("test", i)
#
#
# if __name__ == '__main__':
#     p = Process(target=func)
#     test = Process(target=t2)
#     test.start()
#     p.start()

# 5.线程池的使用
def test(name):
    for i in range(20):
        print(name, i)


if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(4) as t:
        for i in range(5):
            t.submit(test, name=f"线程{i}")
    print("test...")
