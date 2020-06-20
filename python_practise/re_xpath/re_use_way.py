#coding:utf-8 

import re 
"""
# v1
# 查找数字
# \d 代表一个数字 
# + 至少出现一次
p = re.compile(r'\d+') 
s = 'one12two34'
# 在s种进行查找,按照规则p制定的正则进行查找
# 参数3，6表示在字符串种查找的范围
pattern = p.match(s,3,5)
print (pattern)
print (pattern[0])
# <re.Match object; span=(3, 5), match='12'>
# 上述代码说明问题
# match可以输入参数表示起始位置,表示第一次进行匹配成功的内容
"""


"""
# v2
#I表示忽略掉大小写
# 分为两组 
r = re.compile(r'([a-z]+) ([a-z]+)',re.I) 
m = r.match("I am really want make money")
print (m[0])
# I am
print (m[1])
# I
print (m[2])
# am 
print (m.group(1)) 
# I
print (m.group(2))
# am 

""" 



"""
# v3
p = re.compile(r'(\d+)([a-z]+)(\d+)',) 
m = p.search('onetwo123threefour34')
print (m.group())

"""

# v4


p = re.compile(r'[a-z]+$') 
s = 'onetwo12threefour'
m = p.search(s)
print (m.group()) 

n = p.sub(r'fivesix',s) 
print (n)

"""
# v5
# \w匹配字母或数字或下划线或汉字 等价于‘[A-Za-z0-9_]’
# \w+表示匹配数字,字母,下划线和加号本身字符
p = re.compile(r'([a-z]+) ([a-z]+)') 

s = 'hello 123 wang 456 xiaojing, fuck you' 

# 将匹配到的fuck you 替换成hello world
rst = p.sub(r'hello world',s) 

print (rst)
# hello 123 wang 456 xiaojing, hello world
m = p.search(rst)
print (m.group())
# hello world
""" 

"""
# v6
title = u'世界 你好,hello moto' 
p = re.compile(r'[\u4e00-\u9fa5]+') 
m = p.findall(title) 
print (m)
# ['世界','你好']

""" 

# v7
"""
#贪婪 
title = u'<div>name</div><div>age</div>' 
p1 = re.compile(r'<div>.*</div>') 
m1 = p1.search(title) 
print (m1.group())
# <div>name</div><div>age</div>

# 非贪婪
p2 = re.compile(r'<div>.*?</div>') 
m2 = p2.search(title) 
print (m2.group())
# <div>name</div>
"""