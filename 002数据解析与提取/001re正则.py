
# 使用re的 目的 是进行数据的 解析 与 提取

# 导入re
import re

# 定义正则
regex = r"\d+"

# 定义要解析的字符串
parseStr = "我的电话是：10023，她的电话是：10098"

# 1.使用findall()进行爬取  [这种方式不建议}
# 匹配字符串中所有的符合正则的内容
list = re.findall(regex, parseStr)
# print(list) ['10023', '10098']



# 2.使用finditer()进行爬取
# 匹配字符串中所有的内容[返回的是迭代器，迭代器效率高]  从迭代器拿到的数据要.group()
iter = re.finditer(regex, parseStr)
for i in iter:
    print(i.group())

# 输出结果  10023
#          10098


# 3.re.search(),全文检索，查到一个就返回，只会返回一个
ser = re.search(regex, parseStr)
# print(ser.group()) 10023



# 4 re.match() 从开头进行匹配  所以返回None
# match的regex相当于 r"^\d+"
mat = re.match(regex, parseStr)
# print(mat)  None

# 5. 预加载正则表达式
test = re.compile(regex)
res = test.finditer(parseStr)
for it in res:
    print(it.group())

# 输出结果  10023
#          10098




# 模拟一个html案例
s = """
<div class='joy'><span id='1'>张天爱</span></div>
<div class='jl'><span id='2'>刘亦菲</span></div>
<div class='zy'><span id='3'>周也</span></div>
<div class='mzy'><span id='4'>孟子义</span></div>
<div class='jsy'><span id='5'>江疏影</span></div>
"""
# 预加载正则表达式
# (?P<名字>正则表达式) 可以单独从正则表达式中提取内容
reg = re.compile(r"<div class='.*?'><span id='\d+'>(?P<name>.*?)</span></div>", re.S) # re.S 让.能匹配换行符

result = reg.finditer(s)
for it in result:
    print(it.group("name"))
# 结果
# 张天爱
# 刘亦菲
# 周也
# 孟子义
# 江疏影























