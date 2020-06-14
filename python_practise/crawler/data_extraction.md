# 页面解析和数据提取

-结构数据:先有结构,再谈数据
--json数据
--转换成python类型进行操作(json类) 
--XML文件
---转换成python类型(xml to dict) 
---XPath
---CSS选择器
---正则


-非结构化数据: 现有数据,再谈结构
-- 文本/邮箱地址/电话号码
-- 通常处理此类数据,使用正则表达式 
--HTML文件 
---正则
---XPath 
---CSS选择器


# 正则表达式
- 一套规则,可以在字符串文本中进行搜查替换等 

*? 重复任意次，但尽可能少重复  
+? 重复1次或更多次，但尽可能少重复  
?? 重复0次或1次，但尽可能少重复  
{n,m}? 重复n到m次，但尽可能少重复  
{n,}? 重复n次以上，但尽可能少重复

-v1: re的基本使用流程
- match的基本使用

-正则常用方法:
--match : 从开始位置开始查找,一次匹配v1
--search : 从任何位置查找,一次匹配  案例 v2
-- findall : 全部匹配, 返回列表    v3
-- finditer: 全部匹配, 返回迭代器   v3
-- split : 分割字符串,返回列表 
-- sub : 替换

-匹配中文: 
 - 中文unicode范围主要在[u4e00-u9fa5]  v4 


-贪婪与非贪婪: 
--贪婪模式: 在整个表达式匹配成功的前提下,尽可能多的匹配
--非贪婪模式: xxxxxxxxxxxxxxxxx,尽可能少的匹配
--python里面数量词默认是贪婪模式 
--例如: 
--- 查找文本 abbbbbbbbbccccc
    re是 ab* 
    如果是贪婪模式下:  abbbbbbbbb
    非贪婪下: 
    (在量词后面直接加上一个问号？就是非贪婪模式。) 


-XML (理解成标签)
-- XML 
--官方文档: http://www.w3school.com/cn/xml/index.asp
--案例 : 见practise.xml 
--概念: 父节点,子节点,先辈节点,兄弟节点,后代节点 

-XPath（XML path language）,是一门在xml文档中查找信息的语言 
--文档: w3school.com.cn/xpath/index.asp 
-Xpath开发工具: le
--开源的xpath表达式工具: XMLQuire 
--Chrome插件: xpath Helper 
--Firefox插件: XPath Checker 

--常用路径表达式: 
--- nodename: 选取此节点的所有子节点 
--- /: 从根节点开始选
--- // : 选取元素,而不考虑元素的具体位置 
--- . : 当前节点 
--- .. : 父节点 
--- @ : 选取属性 

-案例:  
 --bookstore: 选择bookstore下的所有子节点 
 -- /bookstore :  选取根元素 
 -- bookstore/book : 选取bookstore的所有为book的子元素 
 -- //book : 选取book元素 
 -- //@lang : 选取名称为lang的所有属性 

- 谓语(predicates) 
--谓语用来查找某个特定的节点,写方括号中 
-- /bookstore/book[1]: 选取属于bookstore下叫book的元素 
-- /bookstore/book[last()]: 选取最后一个属于bookstore下叫book的元素 
-- /bookstore/book[last()-1]: 选取倒数第二个属于bookstore下叫book的元素 
-- /bookstore/book[position()<3]: 选取属于bookstore下叫book的前两个元素 
-- /bookstore/book[@lang]: 选取属于bookstore下叫book,含有属性lang元素 
-- /bookstore/book[@lang='cn']：选取属于bookstore下叫book的,含有属性lang的值是cn的元素 
-- /bookstore/book[@price > 90] : 选取属于bookstore下叫book的,含有属性price的，且值大于90 
-- /bookstore/book[@preice > 90]/title : 选取属于bookstore下叫book的,含有属性price的,且值小于90的元素title 

-通配符； 
 -- * : 任何元素节点 
 -- @* : 匹配任何属性节点
 -- node() : 匹配任何类型节点 


-选取多个路径 ；
-- //book/title | //book/author : 选取book元素中的title和author元素 
-- //title | //price : 选取文档中所有的title和price元素 



-lxml库: 
-python的html/xml的解析器
-案例 
    v6 解析htmnl :
            html=etree.HTML(XML) 
            result = etree.tostring(html).decode()
    v7 文件读取，:  
        etree只能读取xml文件，读取html文件会报错 

    v8 etree和XPath的配合使用



-beautiful soup : 
--数据提取:

CSS选择器 : BeautifulSoup4 

-几个常用提取信息工具的比较: 
--正则: 很快,不好用
--Beautifulsoup: 慢,使用简单
--lxml: 比较快,使用简单

v9 用beautifulsoup 提取数据 

