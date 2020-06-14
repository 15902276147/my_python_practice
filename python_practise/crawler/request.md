Request

-http for Humans,更简洁,更友好 
-继承了urllib的所有特征
-底层使用了urllib3 
-开源
-文档: http://docs.python-requests.org/zh_CN/latest/index.html

--get 请求:
---requests.get(url) 
---requests.request("get",url) 
---可以带有headers和parmas参数
---v1 

-get返回内容: 
--v2

-post: 发送数据 
-- res = requests.post(url,data=data) 
-- data,headers 要求dict类型 

-proxy 代理: 

    proxies = {
        'http':'adderss of proxy',
        # or 
        'https' : 'adderss of proxy'
    } 

    rep = requests.post("get","http:xxxxxx",proxies) 

--代理有可能出错,如果ip使用人数多,考虑安全问题,可能会被强行关闭 


-用户验证: 
--代理验证
    可能需要使用http basic Auth，可以这样: 
    proxy = {
        #格式为用户名,密码@代理地址:端口地址
        'http':'China:123456@192.168.1.123:4444' 
    } 
    rep = requests.get('http://www.baidu.com',proxies=proxy) 

--web客户端验证: 
    如果遇到web客户端,需要添加auth= (用户名,密码) ---公用wifi

    autu = ('test1',"123456")#授权信息 
    rsp = requests.get("http://www.baidu.com",auth=auth) 


-cookie 
--requests可以自动处理cookie信息 

    rsp = reuqests.get('http://xxxxxxx') 

    #如果对方服务器给传送过来的cookie信息,则可以通过反馈的cookie属性得到 
    #返回一个cookiejar实例 
    cookiejar = resp.cookies

    #可以将cookiejar转换成字典 
    cookie_dict = requests.utils.dict_from_cookiejar(cookiejar) 

--session 
---跟服务器端session不是一个东西 
---模拟一次回话,从客户端浏览器链接服务器开始,到客户端浏览器断开 
---能让我们跨请求时保持某些参数,比如在同一个session实例发出的,所有请求之间保持cookie

    #创建session对象,可以保持cookie值
    ss = requests.session() 
    headers = {
        'User-Agent':'xxxx'
    }
    data = {'name':"xxxx"} 

    #此时,由创建的session管理请求,负责发出请求 
    res = ss.post(url,data,headers) 

-https请求验证ssl证书. 
--参数verify负责表示需要验证ssl证书,默认是true
--如果不需要验证ssl证书,则设置成false表示关闭 

    resp = requests.get(url,verify=False) 

    #如果用verify= True访问http,会报错,因为证书有问题
    

