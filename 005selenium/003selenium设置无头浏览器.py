
# 无头浏览器就是 让Chrome浏览器以静默方式去运行
# 爬取的数据是艺恩网

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

# 准备无头浏览的参数
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")

# 加入参数后，浏览器已静默方式启动
web = Chrome(options=opt)
url = "https://ys.endata.cn/Information/Publish/WillSHow"
web.get(url)
# 获取页面代码
print(web.page_source)



# 定位到下拉列表
# sel = web.find_element(By.XPATH, '//*[@id="app"]/section/main/div/div[1]/div/section/div[1]/div[2]/div/div[1]/div[1]/div/div/input')
# 使用Select()进行包装
# res_sel = Select(sel)
# 让浏览器调整选项(选取不同的options）
# for item in range(len(res_sel.options)):  #item是每个下拉选项索引的位置
    # 按照索引进行切换
    # res_sel.select_by_index(item)
    # 进行下一步解析


