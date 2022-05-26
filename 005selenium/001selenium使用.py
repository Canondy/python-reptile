
# 自动化测试工具： selenium
# 安装selenium  pip install selenium
# 下载浏览器驱动  https://chromedriver.chromium.org/home   选择跟浏览器相对应的版本，https://chromedriver.chromium.org/downloads
# 然后解压，得到 chromedriver 文件，把它放到python解释器所在的文件夹下  /Users/liuhuan/PycharmProject/python-learn/test/venv/bin/   放到bin下

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 简单实现 打开网百度
# 1.创建浏览器对象
# web = Chrome()
# url = "http://www.baidu.com"
# 2.打开网址
# web.get(url)
# 3.输出网址标题
# print(web.title)


# 案例：爬取拉钩网 岗位信息
# 1.创建浏览器对象
web = Chrome()
url = "http://lagou.com"
# 2.打开网站
web.get(url)


# 选择城市
# web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[1]/a') 过时，
# 使用web.find_element(By.XPATH, '//*[@id="changeCityBox"]/ul/li[1]/a')
butt = web.find_element(By.XPATH, '//*[@id="changeCityBox"]/ul/li[1]/a')
# 找到按钮，调用点击事件
butt.click()

# 睡一秒，等待之前操作完成
time.sleep(1)

# 获取输入框，输入要查询的内容，并点击事件
content = web.find_element(By.XPATH, '//*[@id="search_input"]')
content.send_keys("爬虫", Keys.ENTER)

# 睡一秒，等待上一次操作结束
time.sleep(1)

# 这两种获取方式都可以
# list_all = web.find_elements(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[3]/div/div[1]/div')
list_all = web.find_elements(By.XPATH, '//*[@id="jobList"]/div[1]/div')
for item in list_all:
    # 岗位名称
    title = item.find_element(By.XPATH, './div[1]/div[1]/div[1]/a').text.replace("\n", "")
    # 金额
    money = item.find_element(By.XPATH, './div[1]/div[1]/div[2]/span').text
    # 公司
    compony = item.find_element(By.XPATH, './div[1]/div[2]/div[1]/a').text
    # 可以把结果写到文件中
    print(title, money, compony)




# 测试
"""
web.get("https://www.lagou.com/wn/jobs?labelWords=&fromSearch=true&suginput=&kd=java")
all_list = web.find_elements(By.XPATH, '//*[@id="jobList"]/div[1]/div')
all_list = web.find_elements(By.XPATH, '//*[@id="jobList"]/div[1]/div[1]')
for item in all_list:
    # 岗位名称
    title = item.find_element(By.XPATH, './div[1]/div[1]/div[1]/a').text.replace("\n", "")
    # 金额
    money = item.find_element(By.XPATH, './div[1]/div[1]/div[2]/span').text
    # 公司
    compony = item.find_element(By.XPATH, './div[1]/div[2]/div[1]/a').text
    print(title)
"""