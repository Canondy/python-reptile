
# 防盗链 问题    1 ->2 ->3   必须按照顺序访问才可以成功，
# 如果直接访问————2链接————就会出现问题，  访问————链接2————必须添加————链接1————的地址

# 1.拿到contId
# 2.请求https://www.pearvideo.com/videoStatus.jsp?contId=1762556&mrd=0.6891081089328521返回 JSON数据，并获取srcUrl
# 3.srcUrl进行调整，变成实际的视频下载地址
# 4.下载视频

# 导入requests
import requests

# url 是视频所在的页面
url = "https://www.pearvideo.com/video_1762556"
contId = url.split("_")[1]

# targetUrl是视频的下载地址
# 通过请求这个地址https://www.pearvideo.com/videoStatus.jsp?contId=1762556&mrd=0.6891081089328521
# 可以拿到下载地址https://video.pearvideo.com/mp4/adshort/20220521/cont-1762556-15883159_adpkg-ad_hd.mp4
targetUrl = fr"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.6891081089328521"

# 处理防盗链及反爬机制
header = {
    # 模拟浏览器发送请求
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
    # 处理防盗链问题
    # 防盗链 问题    1 ->2 ->3   必须按照顺序访问才可以成功，
    # 如果直接访问————2链接————就会出现问题，  访问————链接2————必须添加————链接1————的地址
    "Referer": url
}

# 通过requests请求获得下载地址
resp = requests.get(targetUrl, headers=header)

# 取整个json结果
result = resp.json()

# 取时间戳
systemTime = result['systemTime']

# 取返回结果里面的srcUrl地址链接
# 这个链接并不是下载视频 的地址
resUrl = result['videoInfo']['videos']['srcUrl']

# 处理resUrl
# 把systemTime 换成cont-{contId}
downUrl = resUrl.replace(systemTime, "cont-" + contId)

# 使用requests再次请求下载地址
video = requests.get(downUrl).content

# 下载视频
with open("video/a.mp4", mode="wb") as f:
    f.write(video)


