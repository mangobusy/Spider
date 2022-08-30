# 解析原理：
#     1.实例化一个etree对象，且要将被解析的页面源码数据加载到该对象中
#     2.调用etree对象中的xpath方法并结合xpath表达式实现标签定位和内容捕获

# 如何实例化一个etree对象：
#     from lxml import etree
#     1.将本地的html文档中的源码数据加载到该对象中
#         etree.parse(filepath)
#     2.将互联网上获取的源码数据加载到该对象中
#         etree.HTML('page_text')
#     3.xpath('xpath表达式')

# xpath表达式：
#     1./:表示从根节点开始定位，表示的是一个层级
#     2.//:表示多个层级，可以表示从任意位置开始定位
#     3.属性定位：tag[@attrName="attrValue"]   eg://div[@class="song"]
#     4.索引定位：//div[@class="song"]/p[3]  索引是从1开始的
#     5.取文本：
#         /text() 获取标签中直系的文本内容
#         //text() 获取标签中非直系的文本内容（所有的文本内容）
#     6.获取属性：/@attrName

# 中文乱码：
#    1. response = requests.get()
#       response.encoding = 'utf-8'
#    2. xxx.encode('iso-8859-1').decode('gbk')

'''
from lxml import etree
import requests
# if __name__=='__main__':
url = 'https://sz.58.com/ershoufang/?utm_source=sem-360-pc&spm=24593799603.6642780624&PGTID=0d100000-0000-4d62-5646-8a7925754212&ClickID=4'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
response_text=requests.get(url=url,headers=headers).text
with open('./58house','w',encoding='utf-8') as fp:
    fp.write(response_text)
tree = etree.HTML(response_text)
list1 = tree.xpath('//div[@class="list"]//section[@class="list"]/div')
for li in list1:
    title = li.xpath('./a/div[2]/div/div/h3/text()')
    print(title)
'''

'''
if __name__=='__main__':
    url = 'http://pic.netbian.com/4krenwu/'
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    response_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(response_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')

    if not os.path.exists('./帅哥美女'):   # 创建一个文件夹
        os.mkdir('./帅哥美女')

    for li in li_list:
        img_src = 'http://pic.netbian.com/' + li.xpath('./a/img/@src')[0]   # 图片的网址
        img_name1 = li.xpath('./a/img/@alt')[0] + '.jpg'    # 图片名称
        img_name = img_name1.encode('iso-8859-1').decode('gbk')   # 解决名称（中文）乱码的通用方法

        img_data = requests.get(url=img_src,headers=headers).content  # 图片是二进制数据，用.content
        img_path = '帅哥美女/' + img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(img_name + '下载成功')
'''
from selenium import webdriver
from bs4 import BeautifulSoup
import os.path
import requests
from lxml import etree

if __name__=='__main__':
    #url = 'http://wjw.sz.gov.cn/yqxx/'
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    # response_text = requests.get(url=url,headers=headers).text
    browser = webdriver.Chrome()
    browser.get('http://wjw.sz.gov.cn/yqxx/')
    text = browser.page_source
    tree = etree.HTML(text)
    list1 = tree.xpath('//div[@class="newsListRigth AllListCon"]//li')

    if not os.path.exists('./深圳卫健委'):
        os.mkdir('./深圳卫健委')

    for li in list1:
        href = li.xpath('./a/@href')[0]
        title = li.xpath('./a/@title')[0]
        path = '深圳卫健委/'+title+'.txt'

        response_detail_text = requests.get(url=href,headers=headers).text
        tree2 = etree.HTML(response_detail_text)
        content_list = tree2.xpath('//div[@class="news_cont_d_wrap"]//text()')
    # print(content_list)
        content_str = ''
        for content in content_list:
            content_str = content + content_str

        print(content_str)
        with open(path,'w',encoding='utf-8') as fp:
            fp.write(content_str)