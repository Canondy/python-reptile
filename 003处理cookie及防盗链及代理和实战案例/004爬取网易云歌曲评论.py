
# 需求：爬取网易云的歌曲评论
# 爬取的的是这个页面的内容： https://music.163.com/#/song?id=1949025727

# 1.找到未加密的参数   window.asrsea(参数，xxx, xxx, xxx)  window.asrsea(JSON.stringify(i0x), buV3x(["流泪", "强"]), buV3x(Rg5l.md), buV3x(["爱心", "女孩", "惊恐", "大笑"]));
# 2.把参数进行加密(根据网易的加密算法)   params => encText,  encSecKey => encSecKey
# 3.使用requests进行爬取，拿到评论信息

# 安装pycrypto   pip install pycrypto
from Crypto.Cipher import AES
from base64 import b64encode
import json
import requests
import csv

# 请求的url
url = "https://music.163.com/weapi/comment/resource/comments/get"

# 请求的参数 方式POST （通过debug拿到的）
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1949025727",
    "threadId": "R_SO_4_1949025727"
}

# 通过debug可以拿到
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"

i = "xePHU6ydl0VkcZLu"

# 获取encSecKey
def get_encSecKey():
    return "d32302de8a374746c7ca919e3bc8ab800174fcde136e8bc6f17f0bc9c70fada4ac6580cbf5aa763f99409938947e0de85362765701f6c5d11e2893ff97147e0a1e2dd1c55d892a49faa205b0f1fd1a0f77023089d5d0183db455c5fa4c8d3c428505638d91e9067ad0e020937176d96325c0d4e00eb9a705c04cccf173d9159c"

# 获取params  并加密，有两次加密过程
def get_params(data):
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second

def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data

# 模拟网易云加密参数
def enc_params(data, key):
    iv = "0102030405060708"
    data_res = to_16(data)
    # 1.创建加密对象   AES.new() 里面的参数都是根据debug所获得
    enc = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC)
    # 2.加密 加密内容的长度必须是16的倍数
    bs = enc.encrypt(data_res.encode("utf-8"))
    # 转换成字符串返回
    return str(b64encode(bs), "utf-8")

# 请求要爬取的网站，url和参数
resp = requests.post(url, data={
    "params": get_params(json.dumps(data)),
    "encSecKey": get_encSecKey()
})

# 准备写入文件的对象
f = open("video/004data.csv", mode="w")
# 使用csv.writer()构建 csv对象
csv_writer = csv.writer(f)

# 取里面的评论
res = resp.json()["data"]["hotComments"]
# print(res)
for cont in res:
    # 取用户名
    nick_name = cont["user"]["nickname"]
    # 取评论
    content = cont['content']
    # 存入到list
    res = [nick_name, content]
    # 把每一个 res 写入到csv文件中
    csv_writer.writerow(res)