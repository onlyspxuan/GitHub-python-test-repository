#-*- coding = utf-8 -*-
import requests   #
import urllib.error,urllib.request  #制定URL，获取网页数据
import os
from bs4 import BeautifulSoup  #网页解析，获取数据
import re   #正则表达式，进行文字匹配
import xlwt   #进行execl操作
import sqlite3  #进行sqlite数据库操作



def main():
    baseurl = 'https://movie.douban.com/top250?start='
      #创建正则表达式对象，表示规则（字符串的模式）

    #1、爬取网页
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影投票250.xls"
    #2、逐一解析数据
    #3、保存数据

#影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')    #findLink为公共参数
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)   #re.S让换行符包含在字符中


#爬取网页
def getData(baseurl):
    datalist = []
    for  i in range(0,10):  #调用获取页面信息的函数，10次
        url = baseurl + str(i*25)
        html = askURL(url)  #保存获取到的网页源码

    # 2、逐一解析数据
        soup = BeautifulSoup(html,'html.parser')
        for item in soup.find_all('div',class_='item'):  #查找符合要求的字符串，形成列表
         # print(item)   #测试：查看电影item全部信息
            data = []  #保存一部电影的所有信息
            item = str(item)
            #影片详情的链接
            Link = re.findall(findLink,item)[0]     #re库用来通过正则表达式查找制定的字符串

    return datalist





#得到制定一个url的网页内容
def askURL(url):
    head = {   #模拟浏览器头部信息，向豆瓣服务器发送消息（伪装用的）
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
    }
    #用户代理，表示告诉豆瓣服务器，我们是什么类型的 机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）

    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.Request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e,code)
        if hasattr(e,"reason"):
            print(e.reason)
    return  html



#保存数据
def saveData(savepath):
    print ()

if __name__ == "__main__":    #当程序执行时
    #调用函数
    main()