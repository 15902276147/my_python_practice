########################

Xpath 

在xml文件中查找信息的一套规则/语言.根据XML的元素或者属性进行遍历

xpath开发工具
-chrome插件: xpath helper

#########################


########################
-nodename : 选取此节点的所有子节点

- / : 从根节点开始选取

- //: 选取节点，不考虑位置

- . : 选取当前节点
- .. : 选取当前节点的父节点 
- @ : 选取属性 

-xpath中查找一般按照路径方法查找,以下是路径表示方法 

School/Tearcher : 返回teacher节点
//Student: 返回所有student的节点,不考虑位置 
School//Age : 选取School后代中所有age节点 
//@other: 选取other属性
//Age[@Detail]:选取带有属性为detail的age元素 

#谓语 - predicates 

- /School/Student[1]: 选取School下面的第一个Student节点
- /School/Student[last()]:选取school下面的最后一个student节点
- /School/Student[last(-1)]: 选取school下面的倒数第二个student节点
- /School/Student[position()<3]:选取school下面的倒数第二个student节点
- //Student[@score]: 选取带有属性score的student节点
- //Student[@score='99']: 选取带有属性score并且属性值是99的student节点
-//Student[@score]/Age : 选取带有属性scroe的Student节点的子节点age 

