结构化文件存储:为了解决不同operation system之间信息的交换
-xml(可扩展标记语言):
--标记语言:语言中使用<>括起来的文本字符串标记
--可扩展:用户可以自己定义需要的标记
--例如: 
    <Teacher> 
        自定义标记Teacher
        在两个标记之间任何内容都应该跟Teacher相关
    </Teacher>
--xml描述的是数据本身,即数据的结构和语义
--HTML侧重于显示web页面的数据;
  xml描述的是数据本身,即数据的结构和语义. 

--跨平台,描述的仅仅是数据

--xml文档的构成: 
1>处理指令(可以认为一个文件内只有一个处理指令)
-内容是与xml本身处理相关的一些声明或者指令
-必须在第一行
-最多只有一行
-以xml关键字开头,使用的版本
2>根元素(一个文件内只有一个根元素) 
-在整个xml文件中，只有一个根元素
3>子元素
4>属性
5>内容
--表明标签所存储的具体信息
6>注释
--起说明作用的信息
--注释不能嵌套在标签里
--只有在注释的开始和结尾使用双短横线
--三短横线只能出现在注释的开头而不能使用在结尾

--保留字符的处理:
1>xml中使用的符号可能根实际符号相冲突,典型的就是左右<> 
使用实体引用来避免这种情况,转义来保留字符
&gt;表示大于
&lt;表示小于 
2>把含有保留字符的部分放在CDATA块内部;
CDATA把内部信息视为不需要转义:
<![CDATA[ 
    select name,age 
    from Student
    where score > 80 
]]>

3>常用的需要转义的保留字符和对应实体引用
& ： &amp; 
< ： &lt;
> ： &gt; 
' ： &apos;
'' ： &quot;

-XML标签的命名规则: 
--Pascal命名法:用单词表示，第一个字母大写
--大小写严格区分
--配对的标签必须一致

-命名空间 
    为了防止命名冲突，需要给可能产生冲突元素添加命名空间 
    --- xmlns: 
    for example 
    <School xmlns:student="http://my_student" xmlns:room="http://my_room"> 
        <student:Name>jinpeng.li</student:Name>
        <age>23</age> 
        <room:Name>2014</room:Name> 
        <location> 1-23-1 <location>
    </School> 


-xml访问: 

--读取两个技术: SAX,DOM

1.SAX (simple api for xml):
--属于事件驱动的api:读一个xml,读到一个指定的element,用一个触发函数来替换或者显示内容
--利用SAX解析文档设计到解析起和事件处理两部分
--特点: 
1> 快
2> 流式读取:从头开始读,不会回头看,过去就是过去

2.DOM 
--是w3c规定的xml变成的借口
--一个xml文件在缓存中以树形结构保存,读取. 
--用途: 
1>定位浏览xml任何一个节点信息
2>添加删除相应内容 

---minidom
---etree 
-以树形结构来表示xml
-root.getiterator 
-root.iter
-find(node_name) 
-root.findall(node_name) 
-node.tag:node对应的tagname 
-node.text:node的文本值
-node.attrib: node的树形的字典类型的内容

-xml文件写入: 

1>ele.set: 修改属性
2>ele.append: 添加子元素
3>ele.remove: 删除元素 

---------------------------------------------------------------


-json
--在线工具: http://www.w3school.com.cn/json/ 
--轻量级的数据交换格式
--json格式是一个键值对形式的数据集
    
    key : 字符串
    value : str,int,list,json
    json使用大括号包裹
    键值对直接用 , 隔开 


-- python for json : 
--- import json 
json和python的转换;
1>json.dumps() : 对数据编码,把python格式表示称json格式
2>json.loads() : 对数据编码,把json格式转换成python格式

python读取json文件
1> json.dump(): 把内容写入到json文件中
2> json.load(): 把json文件内容以python格式读出 

######简单来说,json.loads是用来读取字符串的，json.load用来读取文件######

