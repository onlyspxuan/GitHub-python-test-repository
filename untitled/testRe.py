#正则表达式：判断字符串是否符合一定的标准
import  re

# #创建模式对象
# pat = re.compile("AA")  #此处AA，是正则表达式，用来验证其他字符串
# m = pat.search("SDFSAAdfd") #search字符串被校验内容
# print(m)


# #没有模式对象
# m= re.search('asd','asdfe') #前面字符串是规则（模板），后面字符串是被校验对象
# print(m)
#
# print(re.findall('[A-Z]+','SDFSghgDFsdER'))


print(re.sub('a','A','sdfaefdfadfera'))   #找到a用A替换，在第三个字符串中查找A

#建议在正则表达式式中，被比较的字符串前面加r，不用担心转义字符的问题
a = r"\aadf\'"