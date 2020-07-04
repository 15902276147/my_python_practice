#1.urllib:

-包含模块: 
-- urllib.request: 打开和读取url 
-- urllib.error : 包含urllib.request产生的常见的错误,使用try捕捉 
-- urllib.parse : 包含解析url的方法 
-- urllib.robotparse: 解析robots.txt文件(哪些不能爬)
        -headers为了防止爬虫冲虚爬网站造成网站瘫痪,所以要携带一些headers头部信息才能访问
        -要获取的data信息,在from data标签中

-网页编码问题解决: 
--chardet:可以自动检测页面文件的编码格式,但是可能有误 
-urlopen的返回对象
--geturl: 返回请求对象的url 
--info: 请求反馈对象的meta信息
--getcode: 返回http code

-request.data 的使用

--访问网络的方法:向服务器查一个数据 
 ---get：利用参数给服务器传递信息,参数为dict,然后用parse编码
 ---post：一般向服务器传递参数使用 
  -----post是把信息自动加密处理
  -----如果使用post信息,需要用到data参数
  -----使用post,意味这http的请求头部可能需要modify 
  ----- Content-Type : application/x-www.from-urlencode 
  ----- COntent-Length : 数据长度
  ----- 简而言之,一旦更改请求方法,请注意其它请求头部信息相适应 
  ----- urllib.parse.urlencode可以将字符串自动转换成上面的  
  ----- 为了更多设置请求信息,单纯通过urlopen函数已经不太好用了, 需要利用
        reuqest.Request类模拟请求实体
        (from data中 就是要发送的数据)

-出错处理. urllib.error 
--- URLError产生的原因: 
    -no network 
    - connect server failed 
    - can not found specified server
    - 是OSError的子类 
--- HTTPError: 是URLError的一个子类(先处理子类后处理父类) 

两者区别: 
 -httperror是对应的HTTP请求的返回码错误，如果返回错误是400以上的,
 则引发httperror
 -urlerror对应的一般是网络出现问题,包括url问题 
 -关系区别： OSError - URLError - HTTPError 

- UserAgent -- (浏览器信息,用户身份,设备系统信息) 判断你是谁,你用的什么浏览器 
    --- UserAgent: 用户代理,简称UA，属于headers的一部分,
            服务器用过UA来判断访问者身份
    ---常见的UA值,使用的时候可以直接复制粘贴(headers中useragent部分),也可以用浏览器访问的时候抓包:
            分类:
            chrome
            1.Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36
            2.Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11
            3.Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16

            Firefox
            1.Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0
            2.Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10

            Opera
            1.Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60
            2.Opera/8.0 (Windows NT 5.1; U; en)
            3.Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50
            4.Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50
            等等
            
    ---设置UA可以通过两个方式: 
        1.heads 
        2.add_header

-ProxyHandler处理 (反反爬虫的常用手段)
    --代理服务器 

-使用代理IP,是爬虫的常用手段 
-获取代理服务器的地址:  
    --www.xicidaili.com
    --www.goubaijia.com 
-代理用来隐藏真是访问中,代理也不允许频繁访问某一个固定网站, 所以, 代理一定要很多很多 
-基本使用步骤：
 1.设置代理地址 
 2.创建ProxyHandler
 3.创建opener
 4.安装opener 

-cookie & session  
 --由于http协议的无记忆性,为了弥补这个缺陷,所采用的一个补充协议 
 -- cookie是发给用户（http浏览器）的一段信息, session是保存在服务器上的对应的另一半信息,用来记录用户信息 
 --cookie 和 session的区别: 
  ---存放位置不用,cookie保存用户,session保存在服务器上
  ---cookie unsafety,session会保存在服务器上一定时间,会有过期时间
  --- 单个cookie保存数据不超过4k,很多浏览器限制一个站点最多保存20个cookie 
        (cookie一般只做身份鉴别,一个凭证更多的信息放在session)
 --session的存放的位置: 
  ---存放在服务器端 
  ---一般情况,session是放在内存中或者数据库中 


-使用cookie登录的方法: 
    1.直接把cookie复制下来,然后手动放入请求头

    2.http模块包含一些关于cookie的模块,通过他们我们可以自动使用cookie 
    -CookieJar 
    ---管理存储cookie,向传出的http请求添加cookie,
        cookie存储在内存中
        CookieJar实例回收后cookie将消失,被销毁掉
    -FileCookieJar
    ---就是一个cookieJar,使用文件管理cookie以一个文件存储(filename,delayload=None,policy=None)
    
    -MozillaCokkieJar
    ---请求头与filecookiejar一样(filename,delayload=None,policy=None) 
        创建与mocilla浏览器cookie.txt兼容的FileCookieJar实例
    -LwpCookieJar(filename,delayload=None,policy=None)
    --- 创建与libwww-perl标准兼容的Set-Cookie3格式的FileCookieJar实例
    --关系是: 
      CookieJar --> FileCookieJar --> MozillaCookieJar & LwpCookieJar 

    -利用cookiejar访问人人 v12 

    -handler是Handler的实例,常用的有: 
        -用来处理复杂请求: 
            每个handler处理属于自己的业务:
                生成cookie的管理器
                创建http请求管理器
                生成https管理器
                最后用一个opener打开即可 

    -cookie作为一个变量(保存内存中),打印出来 v14
        -- cookie的属性: 
         ---name:名称
         ---value: 值
         ---domain:可以访问cookie的域名
         ---path: 可以访问cookie的页面路径
         ---expires: 过期时间
         ---size: 大小 
         ---http字段 

    -cookie的保存 - FileCookieJar，v15
    -cookie的读取.  v16 

-SSL 安全层的一种协议 
--SSL证书就是指遵守SSL安全套阶层协议的服务器数字证书(SercureSocketLayer); 
--without ssl 浏览器会显示不安全，因为HTTP协议属于明文协议传输。所以建议网站启用SSL证书，确保自己的网站与用户安全。
--通过SercureSocketLayer,传输数据时就可以加密,
--带有https:的都是使用ssl协议,
--CA(certifacateAuthority)是数字证书认证中心,是发放,管理,废除数字证书的收信人的第三方机构,
--有些网站没有获得第三方认证,比如12306.com，遇到不信任的ssl证书,需要单独处理,用代码忽略掉
--v17

-js加密  
--有的反爬虫策略采用jc对需要传输的数据进行加密处理(通常是取md5值)
--需要加密,传输的就是密文,但是加密函数或者过程一定实在浏览器完成,也就是一定会把代码
(jc code)暴露给user,通过阅读加密算法,就可以模拟出加密过程,从而达到破解. 
明文通过一系列加密算法转换成密文
--过程参看v18
---把加密算法转换成python代码. salt , sign 

-ajax请求
--ajax请求相当于一个页面滑动滚轴可以不断得向下拉取
--异步请求 
--一定会有url,请求方式,可能有数据
--一般使用json格式
--v20 爬取豆掰电影









