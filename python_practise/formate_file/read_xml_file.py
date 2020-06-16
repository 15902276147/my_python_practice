#coding:utf-8 

__author__ : 'jinpeng.li'

import xml.etree.ElementTree 
"""
root = xml.etree.ElementTree.parse('Practise.xml') 

print ('利用getiterator访问') 

ele_student= root.find("Student") 
print (ele_student)
print (ele_student.tag) 
# output: student 

for ele in ele_student: 
    if ele.tag == 'name' : 
        print (ele.text)
        # output : jinpeng.li 

    for sub in ele.getiterator(): 
        if sub.text == 'jinpeng.li': 
            print (sub.tag)
"""


# 解析xml文件
root = xml.etree.ElementTree.parse("xml_use_way.xml") 

"""
# 得到xml文件中所有的node
nodes = root.getiterator()
for node in nodes: 
    # print ("{0}----{1}".format(node.tag,node.text   ))
    # 如果node的tag值是name的话就print出对应的文本值 
    if node.tag == 'name': 
        print (node.text)
        # zhenya.liu
        # jinpeng.li
"""

# 得到xml文件中Teacher的info,ele_teacher是一个可迭代对象
ele_teacher = root.find("Teacher") 



for node in ele_teacher : 
    print (node.tag,node.text)
# output:
# name zhenya.liu
# age  30 
# mobile 1201101892
 
 

print ("{0} ---- {1}".format(ele_teacher.tag,ele_teacher.text)) 
# output : Teacher ---- 


if ele_teacher.tag == 'Teacher': 
    for sub in ele_teacher.getiterator(): 
        # node树形的字典类型的内容
        if "desc" in sub.attrib.keys(): 
            # print出Teacher的属性值
            print (sub.attrib['desc'])    
        # output : PythonTearcher 
    


"""
ele_student = root.findall("Student") 
for ele in ele_student: 
    for sub in ele.getiterator(): 
        if sub.tag == 'name': 
            if "other" in sub.attrib.keys(): 
                print (sub.attrib['other'])
        # output: he is the best
"""