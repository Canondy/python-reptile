
# pyquery官方网址：https://pyquery.readthedocs.io/en/latest/
# 安装pyquery  pip install pyquery

# 导入pyquery
from pyquery import PyQuery

html = """ 
    <ul>
        <li class="a"><a href="http://www.baidu.com">百度</a></li>
        <li class="a" id="tb"><a href="http://www.taobao.com">淘宝</a></li>
        <li class="b"><a href="http://www.bytedance.com">字节</a></li>
        <li class="b"><a href="http://www.tenxun.com">腾讯</a></li>
    </ul>
"""

# 调用PyQuery解析，返回的 p 一个PyQuery对象
p = PyQuery(html)

# print(p) #<li><a href="http://www.baidu.com"/></li>
# print(type(p)) # <class 'pyquery.pyquery.PyQuery'> 返回的是一个PyQuery对象

# 1.获取 a 标签, 返回的 a 一个PyQuery对象
# a = p("a")
# print(a) #<a href="http://www.baidu.com"/>
# print(type(a)) #<class 'pyquery.pyquery.PyQuery'> 返回的还是一个PyQuery对象

# 2.链式操作
# a = p("li")("a")
# print(a) #<a href="http://www.baidu.com"/>


# 3.css选择器
# a = p("li a")
# print(a)  #<a href="http://www.baidu.com"/>

# 4.class选择器
# a = p(".a a")
# print(a) #<a href="http://www.baidu.com">百度</a> <a href="http://www.taobao.com">淘宝</a>

# 5.id选择器
# a = p("#tb a")
# print(a)  #<a href="http://www.taobao.com">淘宝</a>

# 6.拿 li中的 a标签的值 和 a标签的属性值
# href = p("#tb a").attr("href")
# text = p("#tb a").text()
# print(href) # a标签的属性值 http://www.taobao.com
# print(text) # a标签的值   淘宝

# 7.多个标签拿属性
# 取ul中所有的 a标签的值 和属性值
item = p("li a").items()
for it in item:
    href = it.attr("href")
    text = it.text()
    # print(text, href)


divTest = """
    <div class="a"><span>test</span></div>
"""

div = PyQuery(divTest)
# text = div("div").text()
# html = div("div").html()
# print(text)  # test
# print(html)  # <span>test</span>


test = """
<HTML>
    <div class="a"><span>test</span></div>
    <div class="b"><span>love</span></div>
</HTML>
"""

res = PyQuery(test)

# 在指定标签对后面 添加标签对
# res("div.a").after("<div>add</div>\n")

# 在指定标签对里面 添加标签对
# res("div.a").append("<a>one</a>")

# 修改标签对里面的属性值
# res("div.a").attr("class", "test")

# 修改标签对里面的属性值
# res("div.a").attr("id", "test")

# 删除整个标签
# res("div.a").remove()

# 删除标签内的 属性 ,如果没有该属性，则报错
res("div.a").remove_attr("class")

print(res)


# 总结：
# 1.PyQuery(选择器)
# 2.items()  多个标签拿属性，需要一个一个处理时使用
# 3.attr(属性值)  一个参数时获取标签内的属性值， 两个参数时，如果有该属性值，则修改，如果没有，则添加
# 4.text()  获取标签内的文本值
# 5.html()  获取标签内的所有内容（包括标签对）
# 6.after() 在指定标签对后面 添加标签对
# 7.append() 在指定标签对里面 添加标签对
# 8.remove() 删除整个标签
# 9.remove_attr()  删除标签内的 属性
