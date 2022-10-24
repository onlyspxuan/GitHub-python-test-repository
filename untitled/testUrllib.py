import urllib.request

# #1、
# #获取一个get请求
# # response = urllib.request.urlopen("https://movie.douban.com/top250?start=")
# response = urllib.request.urlopen("http://www.baidu.com")
# # print (response)
# # print (response.read())
# print (response.read().decode(utf-8))#对获取到的网页圆满进行utf-8解码


# #2、
# #获取一个post请求
# import urllib.parse
#
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding='utf-8')
# response = urllib.request.urlopen("http://httpbin.org/post",data=data) #post请求需要用data来传递封装的数据
# print(response.read().decode('utf-8'))



# #3、
# #超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.001)
#     print(response.read().decode('utf-8'))
# except  urllib.error.URLError as err:
#     print('time out ！！！！')


# # #4、
# #response = urllib.request.urlopen("http://httpbin.org/get",timeout=2)
# response = urllib.request.urlopen("http://www.baidu.com")
# # response = urllib.request.urlopen("https://movie.douban.com/top250?start=")
# # print(response.status)  # .status 查看返回状态
# # print(response.getheaders)  #.getheaders 获取报文中header->reponse header的信息
# print(response.getheader('Server'))  #.getheader('') 获取报文中header->reponse header中具体某一个数据的信息


#5、
# # 针对反爬虫1_httpbin.org
# url = "http://httpbin.org/post" \
#
# #url = 'https://www.douban.com'
# headers = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
# }
# data = bytes(urllib.parse.urlencode({'name':'xuan'}),encoding='utf-8')
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))



# 针对反爬虫2_douban
url = 'https://www.douban.com'
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
}
req = urllib.request.Request(url=url,headers=headers) #data参数可以为空
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))