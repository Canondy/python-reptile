
# scrapy框架  功能：1.高性能的持久化存储  2.异步的数据下载  3.高性能的数据解析  4.支持分布式

# scrapy的使用  安装：pip install scrapy

# 1.创建scrapy的工程：scrapy startproject  项目名称
# 2.切到---项目名称---文件夹   在spiders文件夹下创建爬虫文件
#   命令：scrapy  genspider  文件名称  www.xx.com
# 3.执行工程：scrapy crawl 文件名称


# 1.创建scrapy的工程：scrapy startproject  项目名称     生成的树结构
#                 firstTest
#                     ├── firstTest
#                     │   ├── __init__.py
#                     │   ├── items.py
#                     │   ├── middlewares.py
#                     │   ├── pipelines.py
#                     │   ├── settings.py
#                     │   └── spiders
#                     │       ├── __init__.py
#                     └── scrapy.cfg

# 2.切到---项目名称---文件夹   在spiders文件夹下创建爬虫文件
#   命令：scrapy  genspider  文件名称  www.xx.com     在项目名称文件夹下的项目名称问价加下的spiders下生成  文件名称.py
#   变成一下的树结构
#                 firstTest
#                     ├── firstTest
#                     │   ├── __init__.py
#                     │   ├── items.py
#                     │   ├── middlewares.py
#                     │   ├── pipelines.py
#                     │   ├── settings.py
#                     │   └── spiders
#                     │       ├── __init__.py
#                     │       └── first.py     执行完 2 的名令会生成新文件
#                     └── scrapy.cfg

# 3.执行工程：scrapy crawl 文件名称

# 1.项目firstTest是scrapy简单使用， 爬虫文件first.py 和settings.py 文件的说明及使用
# 2.项目testWeibo是scrapy简单使用， 爬取微博数据 并解析 并存储到本地指定的文件中
# 3.scrapy的s数据持久化存储：
#     一.基于终端指令：
#             命令：scrapy crawl 爬虫文件名称 -o  路径/文件名.类型
#             例子：在 scrapytestWeibo下面执行 crawl weibo -o ./data/weibo.csv      会在testWeibo下面创建文件及目录
#             类型：只能是这几种 ('json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle')
#             要求：只可以将 爬虫文件中parse方法 的返回值存储到本地文本文件中
#             优点：简介高效便捷
#             缺点：局限性比较强（只能存储在本地指定的文件后缀名中）
#     二.基于管道：
#             编码流程：
#               1.数据解析
#               2.在item类中定义相关的属性
#               3.将解析到的数据封装存储到item类型的对象中
#               4.将item类型的对象提交给管道进行数据持久化存储操作
#               5.在管道process_item中要将其接收到的item对象中存储的数据进行持久化存储操作
#               6.在配置文件settings.py中开启管道
#      三.将爬取的数据一份存储到本地xx.csv中，一份存储到数据库中
#              分析: 管道文件中一个管道类对应的是将数据存储到一个平台
#                   爬虫文件提交的item只会给管道文件中第一个被执行的管道类接受
#                   process_item中的  return item   表示将item传递给下一个即将被执行的管道类
#
#              方法：settings.py 的字典ITEM_PIPELINES 中添加一个 管道类配置 ，
#                   在pipelines.py中添加一个管道类类 把数据存到数据库
# 4.基于spider的全站数据爬取：
#       项目：picMeiZI
#       说明：就是将网站中某板块下的全部页码的数据进行爬取
#       需求：爬取 https://www.pximg.com/meinv 网站的图片标题
#       实现方式：
#           自动手动发送请求
# 5.五大核心组件：spider  引擎  调度器  下载器  管道
# 6.请求传参
#        项目：bossJob
#        目标网站：https://movie.douban.com/top250  豆瓣电影评分前250  实现全站爬取
#        使用场景：爬取解析的数据不在同一个页面内 （深度爬取）
#        需求：爬取不同页码中所有的岗位名称，详情页的岗位描述
# 7.图片数据爬取之imagesPipeline
#        基于scrapy爬取字符串类型的数据和爬取图片类型的数据区别：
#               字符串：只需要xpath解析提交给管道进行持久化操作
#               图片：xpath解析出src属性，单独对图片地址发起请求获取二进制类型的数据
#        基于imagesPipeline：
#               只需要将img的src的属性值进行解析，并提交给管道，
#               管道会对图片的src进行请求发送获取图片的二进制类型的数据，帮我们进行持久化存储
#        项目：imgDown
# 8.中间件
#       下载中间件:
#           位置；引擎和下载器之间
#           作用：批量拦截到整个工程发起的所有请求和响应
#           拦截请求：
#               1.UA伪装 process_request
#               2.代理IP process_exception  return request
#           拦截响应：
#               篡改响应数据，响应对象
# 9.项目 ： 爬取网易新闻中的新闻数据（标题和内容）
#         1>. 通过网页新闻首页提取各个板块对应的url地址（不是动态加载的）
#         2>. 每个板块对应的新闻标题都是动态加载的
#         3>. 通过解析出每条新闻详情页的url获取详情页的页面源码，解析新闻内容
# 10.CrawlSpider类：是Spider的子类
#         全站数据爬取：
#               基于Spider类：手动发送请求
#               基于CrawlSpider
#         CrawlSpider使用：
#               创建一个工程：
#               cd 工程下
#               创建爬虫文件CrawlSpider：
#                         命令： scrapy genspider  -t crawl 爬虫文件  www.xxx.com
#                         链接提取器：
#                               作用：根据指定的规则（allow）进行指定链接的提取
#                         规则解析器：
#                               作用: 将连接提取器提取到的链接进行指定规则（callback）的解析
#
# 11.分布式爬虫
#       ~概念：需要搭建一个分布式的集群，让其对一组资源进行分布联合爬取
#       ~作用：提升爬取数据的效率
#       ~如何实现分布式爬取：
#           -安装scrapy-redis的组件
#           -原生的scrapy不能实现分布式爬虫，必须让scrapy结合scrapy-redis组件一起实现分布式爬虫
#           -scrapy-redis组件作用：
#                   可以给原生scrapy框架提供可以被共享的管道和调度器
#           -实现流程：
#                   创建工程
#                   创建一个基于CrawlSpider类型的爬虫文件
#                   修改当前的爬虫文件
#                       导包：from scrapy_redis.spiders import RedisCrawlSpider
#                       将start_url和allowed_domains进行注释
#                       添加新属性 redis_key = 'sun'  可以被共享的调度器对列的名称
#                       编写数据解析相关的操作
#                       将当前爬虫类的父类修改为RedisCrawlSpider
#                   修改配置文件settings:
#                       指定使用可以被共享的管道：
#                             TIEN_PIPELENS = {
#                                 'scrapy.redis.pipelines.redisPipeline': 400
#                             }
#                       指定调度器：
#                               增加一个去重容器类的配置，作用使用redis的set集合来存储请求的指纹数据，从而实现请求去重的持久化
#                               DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#                               # 使用scrapy-redis组件自己的调度器
#                               SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#                               # 配置调度器是否要持久化，也就是当爬虫结束了，要不要清空redis中请求对列和去重指纹的set
#                               #如果是True,（服务宕机后，爬取没有爬过的数据，之前的爬过的数据，不会再次爬取，数据不会重复）就实现了增量式爬取，
#                               SCHEDULER_PERSIST = True
#                       指定redis服务器：
#                                 REDIS_HOST = '127.0.0.1'
#                                 REDIS_PORT = 6379
#                                 REDIS_ENCODING = 'utf-8'
#                    执行工程：
#                        切换到fbsPro/fbsPro/spider目录下
#                        执行命令：scrapy  runspider  爬虫文件(fbs.py)
#                    向调度器中放入一个起始的url：
#                        调度器的对列在redis的客户端中：
#                               在redis客户端中执行命令： lpush  (爬虫文件中的redis_key对应的）sun  爬取的网址
#                                  这个项目的命令： lpush sun  https://movie.douban.com/top250?start=0
#
#