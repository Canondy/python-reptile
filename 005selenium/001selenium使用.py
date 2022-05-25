
# 自动化测试工具： selenium
# 安装selenium  pip install selenium
# 下载浏览器驱动  https://chromedriver.chromium.org/home   选择跟浏览器相对应的版本，
# 然后解压，得到 chromedriver 文件，把它放到python解释器所在的文件夹下  /Users/liuhuan/PycharmProject/python-learn/test/venv/bin/   放到bin下

from selenium.webdriver import Chrome

# 1.创建浏览器对象
web = Chrome()


url = "http://www.baidu.com"
# 2.打开网址
web.get(url)

# 3.输出网址标题
print(web.title)