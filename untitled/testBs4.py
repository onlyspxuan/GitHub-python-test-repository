'''
BeautifulSoup4将复杂的HTML文档转成一个复杂的树形结构，每个节点都是python对象，所有对象都可以归纳为四种：

-Tag   标签
-NavigableString  标签里的内容（字符串）
-BeautifulSoup   表示整个文档
-Comment
'''

from bs4 import  BeautifulSoup


file = open("./baidu.html","rb")  #rb  打开一个文档，二进制的读取
html = file.read()    #读取一个文档，作为一个对象
bs = BeautifulSoup(html,"html.parser")  #使用一个名字叫html.parser 的解析器来解析这个html文档

# print(bs.title)  # 输出html中的title
# #print(type(bs.title))
# print(type(bs.head))
# #1、Tag  标签及其内容：拿到它找到的第一个内容
#
# print(bs.title.string)
# print(type(bs.title.string))
# #2、 NavigableString 标签里的内容（字符串）
# print(bs.a.attrs) #可得到a标签中的所有属性
#
#
# #print(bs)
# print(type(bs))
# #3、BeautifulSoup   表示整个文档
#
#
#
# print(bs.a.string)
# print(type(bs.a.string))
# #4/Comment 是一个特殊的NavigableString，输入的内容不包括注释符号【？？？对Comment有疑问】




#-----------------------------------------------------------


#文档的遍历
print(bs.head.link)

#print(bs.head.content[1])




#文档的搜索

# #(1) find_all
# #字符串过滤：会查找与字符串完全匹配的内容
# t_list = bs.find_all('a')
#
# import re
# #正则表达式搜索：使用search()方法来匹配内容
# t_list = bs.find_all(re.compile('a'))

# #方法：传入一个函数（方法），根据函数的要求来搜索（了解一下即可，可自己定义）
# def name_is_exists(tag):
#     return  tag.has_attr('name')
# t_list = bs.find_all(name_is_exists)  #测试括号中name_is_exists不能带（），否则会报错
#
# for item in t_list:
#     print(t_list)
#
# # print (t_list)

# #(2)kwarg  参数
# # t_list = bs.find_all(id='head')
# t_list = bs.find_all(class_=True)
#
# for item in t_list:
#     print(t_list)


# #（3）text参数
# t_list = bs.find_all(text='牛年贺岁，登录设置新春皮肤！')
# # t_list = bs.find_all(text= ['百科','健康','知道'])
#
# for item in t_list:
#     print(item)


# #(4) limit 参数
# t_list = bs.find_all('a',limit=4)  #限定展示关于a的内容3个
#
# for item in t_list:
#     print(item)
#
# # print(t_list)



#css选择器
# t_list = bs.select('title') #通过标签来查找
#
# t_list = bs.select(".lh") #通过类名来查找   class="lh"
#
# t_list = bs.select("#s_wrap")  #通过id来查找  id="s_wrap"
#
# t_list = bs.select ("a[class='text-color']")  #通过属性来查找  <a class="text-color">关于百度</a>

t_list = bs.select("head > link",limit=4) #通过子标签来查找,    >两端必须要有空格，否则会报错

# t_list = bs.select(".text-color ~  .bri")
# print(t_list[0].get_text())

for item in t_list:
    print(item)

