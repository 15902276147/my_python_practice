正则表达式：
用于使用单个字符串来描述,匹配符合某个规则的字符串
####正则的写法:
.:表示任意一个字符,除了\n，比如查找所有的一个字符 \. 
[]: 匹配中括号中列举的任意字符,比如[L,Y,O],比如LLY,YO 
\d : 匹配任意一个数字. 
\D : 匹配除了数字都可以
\s : 匹配表示空格,tab键
\S : 匹配除了空格符号
\w : 匹配单词字符，就是a-z,A-Z,0-9,_ 
\W : 匹配除了单词字符的都可以
 * : 匹配表示前面内容重复0次或者多次
 + : 表示前面内容至少出现一次 
 ? : 表示前面出现的内容的内容0次或者一次 
{m,n} : 表示前面内容出现最少m次,最多n次
^ : 匹配字符串的开始
$ : 匹配字符串的结尾 
\b: 匹配单词的边界
() : 对正则表达式内容进行分组，从第一个括号开始，编号逐渐增大
\A : 只匹配字符串开头，\Aabcd 则abcd 
\Z : 仅匹配字符串的末尾，abcd\Z,abcd 
| : 左右任意一个
(?P<name>.....) : 分组,除了原来的编号在制定一个别名
(?P=name): 引用分组


for example: 

验证一个数字: ^\d$ 
必须有一个数字，最少一位 : ^\d+$ 
只能出现数字,其位数为5-10位: ^\d{5,10}$ 
注册者输入年龄,要求16岁以上，99以下: ^[16,99]$ 
只能输入英文字符和数字: ^[A-Za-z0-9]$ 
验证qq : [0-9]{5,12}
####

v1:
re使用大致步骤: 
1.使用compile将表示正则的字符串编译为一个pattern对象
2.通过pattern对象提供一系列方法对文本进行查找匹配,获得匹配结果,一个match对象
3.最后使用match对象提供的属性和方法获得信息，根据需要进行操作
v2:
re常用函数： 
-group():获得一个或者多个分组匹配的字符串,直接使用group或者group()
-start:获得分组匹配的字符串在真个字符串种的起始位置，参数默认为0
-end：获取分组匹配的字符串在整个字符串种的结束位置,默认为0 
-span：返回的结构技术(start(group),end(group)) 


-查找用 
在字符串中查找匹配,pos和endpos表示起始位置
-search (str,[pos],[endpos])   v3
-findall:查找所有符合要求的结果都找到,返回列表 v4
-finditer：查找,返回一个iter结果


v5:
-sub 替换
--sub(rep1,str[count]) 

v6:
-匹配中文 
--大部分中文内容表示范围是[u4e00-u9fa5]

v7:
-贪婪:尽可能多的匹配
(*)表示贪婪匹配 
-非贪婪:找到符合条件的最小内容即可. 
(?)表示非贪婪 
-正则默认模式是贪婪 






