# requests模块：模拟浏览器发送请求
# 如何使用：
#   --指定url
#   --发起请求
#   --获取响应数据
#   --持久化储存
import json

import requests
'''
if __name__ == '__main__':
    # 指定url
    url = 'https://www.sogou.com/'
    # 发起请求
    response = requests.get(url = url)  # get方法会返回一个响应对象
    # 获取响应数据
    page_text = response.text  # text返回的是字符串性质的响应对象
    # 持久化存储
    with open('./sougou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
'''


# UA: user-agent 请求载体的身份标识
# UA检测：正常请求--通过浏览器
#        不正常请求--通过爬虫--服务器可能拒绝该次请求
# UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
'''
if __name__ == '__main__':
    # UA伪装：将对应的UA封装到一个字典中
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu'
    # 处理url携带的参数：封装到字典中
    kw = input('enter a word:')
    param = {
        'wd':kw
    }
    response = requests.get(url=url,params=param,headers=headers)
    page_text = response.text
    filename = kw + '.html'
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)
'''
'''
import json
if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    params = {
        'type' : '24',
        'interval_id' : '100 : 90',
        'action' : '',
        'start' : '0',
        'limit' : '20',
    }
    response = requests.get(url=url,params=params,headers=headers)
    list_data = response.json
    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)
'''

import json
if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    city = input('please input a city:')
    params = {
        'cname':'',
        'pid':'',
        'keyword': city,
        'pageIndex': 1,
        'pageSize': 10
    }
    response = requests.get(url=url,params=params,headers=headers)
    response_text = response.text
    fp = open('./KFC.json','w',encoding='utf-8')
    json.dump(response_text,fp=fp,ensure_ascii=False)


# if __name__ == '__main__':
#     url = 'https://rt0.map.gtimg.com/tile'
#     header = {
#        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
#     }
#     params = {
#         'styleid' : 0,
#         'tiles': '14_13346_9273,14_13347_9273,14_13346_9272,14_13347_9272',
#         'version': '1135',
#         'style': 100,
#         'compress': 1,
#         'mapType': 'hybrid'
#     }
#     response = requests.get(url=url,params=params,headers=header)
#     response_text = response.text
#     fp = open('./MDL.json','w',encoding='utf-8')
#     json.dump(response_text,fp=fp,ensure_ascii=False)

if __name__ == '__main__':
    url = 'https://image.so.com/view?q=%E9%82%93%E7%B4%AB%E6%A3%8B&src=tab_www&correct=%E9%82%93%E7%B4%AB%E6%A3%8B&ancestor=list&cmsid=be7d24da5a7d79dc49e585df70ae7dcb&cmras=0&cn=0&gn=0&kn=0&crn=0&bxn=0&fsn=60&cuben=0&pornn=0&manun=6&adstar=0&clw=271#id=04b1b6aff20ac709e1a7aceeeae9fdd3&currsn=0&ps=66&pc=66'
    image_data = requests.get(url=url).text
    with open('./dzq.html','w',encoding='utf-8') as fp:
        fp.write(image_data)