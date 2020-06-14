#coding: utf-8 

__author__ = 'jinpeng.li' 

import re
from urllib import request
from lxml import etree
from urllib import request
from bs4 import BeautifulSoup 

#v1. re的基本使用流程

"""
正则结果match的使用案例 
"""
"""
# 以下正则分成了两个组,以小括号为单位

# [a-z] --> a到z任意一个字母; + -->至少出现1次
s = r'([a-z]+) ([a-z]+)' 

pattern = re.compile(s,re.I) #re.I表示忽略大小写 


m = pattern.match('Hello world wide web') 
print (m)

# group(0) 表示匹配成功的整个字符串
s = m.group(0) 
print (s) 
# Hello world 

a = m.span(0) #返回匹配成功的,整个字符串的跨度 
print (a) 
# (0,11)anli分组匹配成功的字符串
b = m.group(1)
print (b)
# Hello

c = m.span(1) 
print (c) 
# 0-5
anli
d = m.group(2)
print (d) 
# world 

e = m.span(2) 
print (e)
# (6,11)

g = m.groups() 
print (g)
# 返回tuple('Hello','world')
""" 

# v2 search 从任何位置查找,一次匹配
"""
s = r'\d+' 

pattern = re.compile(s) 
anli
m = pattern.search(target_str,0,5) 
print (m.group()) 
# output: 23 
"""

# v3 findall 全部匹配,找出列表 
"""
pattern = re.compile(r'\d+') 

s = pattern.findall("i am 18 years old and 185 high") 

print (s)

#['18','185'] 

m = pattern.finditer("i am 18 years old and 185 high")

for iter in m : 
    print (iter.group())

# 18 
# 185
""" 

# v4  中文编码
"""anli
hello = '你好,世界' 

pattern = re.compile(r'[\u4e00-\u9fa5]+') 

s = pattern.findall(hello) 
anli
# output: ['你好', '世界']
 
""" 

# v5 贪婪非贪婪 
"""
pattern = re.compile(r'a.*c') 

s = pattern.match('abcabc') xt = 

# output : abcabc 

pattern = re.compile(r'a.*?c') 
m = pattern.match('abcabc') 
print (m.group())
""" 

# v6 用lxml库解析xml代码

# text = 
# <dev> 
    # <ul> 
        # <li class = 'item-0'> <a href='0.html'> first item </a></li> 
        # <li class = 'item-0'> <a href='1.html'> first item </a></li> 
        # <li class = 'item-0'> <a href='2.html'> first item </a></li> 
        # <li class = 'item-0'> <a href='3.html'> first item </a></li> 
        # <li class = 'item-0'> <a href='4.html'> first item </a></li> 
    # </ul>
# </dev>


"""
# 利用etree.html把字符串解析成html文档 
html =  etree.HTML(text) 
s = etree.tostring(html).decode()
print (s)
""" 

# v7 
"""
if __name__ == '__main__': 
    
    html = etree.parse('./practice.xml')
    
    result = etree.tostring(html,pretty_print=True).decode()

    print (result)
""" 

# v8 和XPath配合使用 
""" 
if __name__ == '__main__': 

    html = etree.parse('./practice.xml') 
    # xpath的意思是,查找带有category属性值为education的book元素下的year元素
    result = html.xpath('/bookstore/book[@category="education"]/year')
    res = html.xpath('//book') 
    res = res[0] 
    print (res)

    # 将列表的值取出
    res = result[0]
    # 打印出
    print (res.tag)
    # 打印带有category属性值为education的book元素下的year元素的值
    print (res.text)
"""

# beautiful soup 

#coding:utf-8



if __name__ == '__main__' : 
    url = 'https://www.baidu.com' 

    response = request.urlopen(url) 
    content = response.read() 

    soup = BeautifulSoup(content,'lxml')
    # bs自动转码
    result = soup.prettify()

    print (result.decode())   
