
# selenium窗口切换
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1.创建浏览器对象
web = Chrome()
# 2.请求网址
url = "http://www.lagou.com"
web.get(url)
# 3.选择城市 北京  使用.click()方法进行点击
web.find_element(By.XPATH, '//*[@id="changeCityBox"]/ul/li[1]/a').click()
# 4.输入框，要查询的岗位，并调用点击方法.send_keys("想要查询的内容", Keys.ENTER)，进行查询
web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys("java", Keys.ENTER)
# 5.点击岗位标题，访问详情页面  （会打开一个新的tab页）
web.find_element(By.XPATH, '//*[@id="jobList"]/div[1]/div[3]/div[1]/div[1]/div[1]/a').click()
# 6.切换到详情页
web.switch_to.window(web.window_handles[-1])
# 7.在详情页抓取数据，岗位要求
content = web.find_element(By.XPATH, '//*[@id="job_detail"]/dd[2]/div').text
print(content)
# 8.关闭当前tab页窗口
web.close()
# 9.切回到主页面
web.switch_to.window(web.window_handles[0])