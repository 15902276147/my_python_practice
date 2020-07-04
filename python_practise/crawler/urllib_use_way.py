c#coding:utf-8 

__author__ = 'jinpeng.li' 

# Description: the way of use requests 
# 
# v1:使用urllib.reuqest请求一个网页内容,并打印内容

import requests 
from http import cookiejar
from urllib import request,parse,error
import json
import chardet
import ssl

#v1: 
"""
def main(): 
    url = "https://www.baidu.com/"
    #open url and return HTTP reuslt 
    url_info = request.urlopen(url) 
    #read result 
    # the type of result's content is bytes,need decoding.
    html = url_info.read() 
    result_html = html.decode("utf-8") 
    print (result_html)

if __name__ == '__main__':
    main()
"""
#v2:自动检测页面编码 
"""
if __name__ == '__main__': 

    url = 'https://www.baidu.com/'
    response = request.urlopen(url).read() 
    
    #利用chardet自动检测
    cs =  chardet.detect(response)
    print (type(cs)) # -- dict 
    print (cs) 
    #使用get取值保证不会出错,如果检测不到,就默认utf-8
    result = response.decode(cs.get("encoding","utf-8")) 
    print (result)

"""

#v3: urlopen的返回对象 
"""
if __name__ == '__main__': 
    url = 'https://www.baidu.com' 

    response = request.urlopen(url) 
    
    print (type(response))
    print (response) 
    print ("url:{}".format(response.geturl()))
    print ("INFO: {}".format(response.info())) 
    print ('Code: {}'.format(response.getcode())) # 200-成功　404 - not found 
"""


#v4 request.data的使用(向服务器查数据)
#对url进行参数编码的方式,需要用parse模块
"""
if __name__ == '__main__': 
    #s?---> 参数
    url = 'https://www.baidu.com/s?' 
    
    #想要查询的content
    wd = input('Input your keyword:') 

    #要使用data,需要使用字典结构 (wd就是参数)
    qs_info = {
        "wd": wd
    }    
    #对dict 转换url编码
    qs_obj  = parse.urlencode(qs_info)
    print (qs_obj)

    target_url = url + qs_obj
    
    print (target_url) 

    #如果直接用可读的带参数的url,是不能访问的
    response_info = request.urlopen(target_url).read() 

    chardet_test = chardet.detect(response_info) 
    
    request_obj = response_info.decode(chardet_test.get("encoding","utf-8")) 
    
    print (request_obj)
"""




#v5 百度翻译 
"""
利用parse模块模拟post请求 
分析百度词典
1.分析步骤: 
1.F12打开developer-tool
2.尝试输入单词girl,发现没敲一下字母后都有请求 
3.请求地址是  https://fanyi.baidu.com/sug
4.利用network-ALL-Hearders，查看发现form data的值是 kw:girl
5.检查返回内容格式,发现返回的是json格式,需要用到json模块 

2.大致流程: 
1. 利用data构造内容,然后urlopen打开 
2. 返回一个json格式的结果
3. 结果应该是girl的中文意思
"""

"""
base_url = "http://fanyi.baidu.com/sug"


#存放用来模拟form的数据一定是dict格式(硬性规定)
data = {
    #girl是翻译输入的英文内容,应该是由用户输入,此处硬编码
    'kw' : 'girl'     
}


#需要使用parse模块对data进行编码 
data = parse.urlencode(data).encode('utf-8') 

#有了data,url,就可以尝试发出请求了
#urlopen没有headers的参数
response = request.urlopen(base_url,data=data).read() 

json_info = response.decode("utf-8") 
json_obs = json.loads(json_info) 


for key,item in json_obs.items(): 
    if key == "error": 
        print (item)
"""

#v6 urllib.request.Request 
"""
base_url =  "https://fanyi.baidu.com/sug"
#要获取的data信息,在from data标签中
data = {
    "kw" : 'girl' 
}
data = parse.urlencode(data).encode('utf-8')
#headers为了防止爬虫冲虚爬网站造成网站瘫痪,所以要携带一些headers头部信息才能访问
headers = {
    #要放数据,post请求至少要包括Content-Length
    'Content-Length': len(data)
} 
#构造一个Request的实例
res = request.Request(base_url,data = data,headers=headers) 

#因为已经构造了一个Request请求实例,则所有的请求信息都可以封装在Request实例中
response = request.urlopen(res).read() 
cs = chardet.detect(response) 
request_result = response.decode(cs.get("encoding","utf-8")) 
request_json_info = json.loads(request_result) 
for item in request_json_info['data']: 
    print (item['k'],"---",item['v']) 
""" 

#v7,8  URLError,HttpError的使用
"""
if __name__ == '__main__': 

    url = "http://www.sipo.gov.cn/www" 

    try: 
        res = request.Request(url) 
        response = request.urlopen(res).read() 
        result = response.decode("utf-8")
        print (result) 

    except error.HTTPError as e : 
        print ("HTTPError:" + str(e))

    except error.URLError as e : 
        print ("urlerror:" + str(e.reason)) 

    except Exception as e : 
        print ("error:"+str(e))
"""

#v9访问baidu,更改自己的UA进行伪装
"""
if __name__ == '__main__': 
    url = 'http://www.baidu.com' 
    try: 
        #使用headers方法伪装UA
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'
        res = request.Request(url=url,headers=headers)  
        #正常访问
        response = request.urlopen(res).read() 

        result = response.decode('utf-8') 

        print (result) 
    except error.HTTPError as e : 
        print ('Http error:' + str(e)) 
    
    except error.URLError as e : 
        print ('url error:' + str(e)) 
    
    except Exception as e : 
        print (str(e))
    
    print ('Done.....')

""" 
#v10使用add_headers方法 
"""
if __name__ == '__main__': 
    url = 'http://www.baidu.com' 

    try:
        res = request.Request(url) 
        res.add_header("User-Agent","Opera/8.0 (Windows NT 5.1; U; en)")

        response = request.urlopen(res).read() 
        cs = chardet.detect(response) 
        result = response.decode(cs.get("encoding","utf-8")) 


        print (result) 

    except error.HTTPError as e : 
        print (str(e)) 
    
    except error.URLError as e : 
        print (str(e)) 

    except Exception as e : 
        print (str(e)) 
    
    print ("Done.......")
"""

#v10. ProxyHandler代理服务器访问百度
"""
if __name__ == '__main__': 
    
    url = 'http://www.baidu.com' 
    
    #1.设置道理地址,是一个dict
    proxy = {'https':'113.121.245.32'} 
    #2.创建ProxyHandler 
    proxy_handler = request.ProxyHandler(proxy)
    #3.创建opener
    opener = request.build_opener(proxy_handler)
    #4.安装opener
    request.install_opener(opener) 

    #现在如果访问url,使用代理服务器
    
    try :  
        response = request.urlopen(url).read() 
        result = response.decode('utf-8') 
        print (result) 
    except error.HTTPError as e : 
        print ('http error:' + str(e))
    
    except error.URLError as e : 
        print ('url error:' + str(e)) 

    except Exception  as e : 
        print (str(e))
""" 

#v10 模仿没有cookie登录 
"""
if __name__ == '__main__': 
    

    url = 'https://v.qq.com/' 

    try : 
        rsp = request.Request(url) 
        response = request.urlopen(rsp).read() 
        result = response.decode('utf-8') 
    
    except error.HTTPError as e : 
        print ('http error :' + str(e))
    
    except error.URLError as e : 
        print ('url error:' +str(e)) 
    except Exception as e : 
        print (str(e))

    with open('result.html','w') as f : 
        f.write(result) 
        print ('Done....') 
""" 
 
#v11 包含cookie登录 
"""
if __name__ == '__main__' : 

    url = 'https://v.qq.com/' 
    
    headers = {
        "Cookie" : "pgv_pvi=2740979712; RK=dB5Miw9CUl; ptcz=ab2530ed4228f2a2ed6a420a90303e6bf8a012e47909718b44e95311f95d9cfb; tvfe_boss_uuid=6fa9fa30075b79b3; pgv_pvid=2387346760; ts_uid=9830847533; ts_refer=www.baidu.com/link; tvfe_search_uid=d7965bd3-80a9-487a-bc44-d11c18d05c8c; pgv_info=ssid=s3053889072; pgv_si=s6099978240; main_login=qq; vqq_vuserid=16781021; vqq_access_token=35677500D1E163A14DE32F9F1FBB3238; vqq_openid=DF539F7478023C6D4B3AA8F6EC210955; vqq_appid=101483052; video_guid=526585201df11f07; video_platform=2; qq_nick=%E9%BA%BB%E7%93%9C; qq_head=http://thirdqq.qlogo.cn/g?b=oidb&k=PxSw51zgLvjTwbicjpafe9w&s=640&t=1569298158; login_remember=qq; webwx_data_ticket=gSeJJzuW4c9+VIgMO4cmFVdJ; AMCVS_248F210755B762187F000101%40AdobeOrg=1; AMCV_248F210755B762187F000101%40AdobeOrg=-1712354808%7CMCIDTS%7C18406%7CMCMID%7C86183540425548567054272097770851600666%7CMCAAMLH-1590851188%7C11%7CMCAAMB-1590851188%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1590253588s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.3.0; s_cc=true; tp=2586; s_ppv=cn%253Anews%253Aarticle%2C99%2C99%2C2557; vqq_vusession=rgbq9rV_nm2lVFjMSNiw6A..; ptag=www_baidu_com; ad_play_index=34; bucket_id=9231006; ts_last=v.qq.com/; uid=150136142; qv_als=nth/vrOIVxZavkTIA1159042019163S/Ww=="
    }
    
    try : 
        rsp = request.Request(url,headers=headers) 

        response = request.urlopen(rsp) 

        result = response.read().decode('utf-8')

        with open('result.html','w') as f : 
            f.write(result) 
            print ('Done....')  
    except error.HTTPError as e : 
        print ('http error :' + str(e))
    
    except error.URLError as e : 
        print ('url error:' +str(e)) 
    except Exception as e : 
        print (str(e))
"""

#v12.自动使用cookie登录,大致流程是
# 打开登录页面后自动通过用户名密码登录
# 自动提取反馈回来的cookie
# 利用提取的cookie登录隐私页面 
"""
# 创建cookiejar的实例
cookie = cookiejar.CookieJar() 
# 生成cookie的管理器 
cookie_handler = request.HTTPCookieProcessor(cookie) 
# 创建http请求管理器 
http_handler = request.HTTPHandler() 
# 生成https管理器
https_handler = request.HTTPSHandler() 
# 创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def log_in():
    # 负责初次登陆
    # 需要输入用户名和密码,用来获取登录cookie凭证
    
    # 此url需要从登录form的action属性中提取
    url = "http:www.renren.com/Plogin.do" 
    # 此键值需要从登录form的两个对象input中提取name属性
    data = {
        'email':'15902276147',
        'password':'123456'
    }
    #把data编码
    data = parse.urlencode(data).encode('utf-8')
    # 创建请求对象
    res = request.Request(url,data=data) 
    # 发起请求
    response = opener.open(res) 

def get_home_page(): 
    target_url = 'http://www.renren.com/965187997/profile' 
    # 如果已经执行了login函数,则opener自动已经包含相对应的cookie值
    rep = opener.open(target_url) 

    result = rep.read().decode('utf-8') 
    
    with open('result.html','w') as f : 
        f.write(result) 
if __name__ == '__main__': 
    log_in() 
    get_home_page() 
""" 

# v14
"""
# 创建cookiejar的实例
cookie = cookiejar.CookieJar() 
# 生成cookie的管理器 
cookie_handler = request.HTTPCookieProcessor(cookie) 
# 创建http请求管理器 
http_handler = request.HTTPHandler() 
# 生成https管理器
https_handler = request.HTTPSHandler() 
# 创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def log_in():
    # 负责初次登陆
    # 需要输入用户名和密码,用来获取登录cookie凭证
    
    # 此url需要从登录form的action属性中提取
    url = "http:www.renren.com/Plogin.do" 
    # 此键值需要从登录form的两个对象input中提取name属性
    data = {
        'email':'15902276147',
        'password':'123456'
    }
    #把data编码
    data = parse.urlencode(data).encode('utf-8')
    # 创建请求对象
    res = request.Request(url,data=data) 
    # 发起请求
    response = opener.open(res) 

if __name__ == '__main__': 
    # 执行完login之后,会得到授权之后的cookie 
    # 尝试把cookie打印出来 
    log_in() 

    print (cookie) 
    for item in cookie: 
        print (type(item)) 
        print (item) 
        for i in dir(item): 
            print (i)
    
""" 

# v15 - 使用FileCookiJar 
"""
#创建filecookiejar
filename = 'cookie.txt'

# 创建cookie实例
cookie = cookiejar.MozillaCookieJar(filename=filename) 

# 生成cookie的管理器 
cookie_handler = request.HTTPCookieProcessor(cookie) 
# 创建http请求管理器 
http_handler = request.HTTPHandler() 
# 生成https管理器
https_handler = request.HTTPSHandler() 
# 创建请求管理器
opener = request.build_opener(http_handler,https_handler,cookie_handler)

def log_in():
    # 负责初次登陆
    # 需要输入用户名和密码,用来获取登录cookie凭证
    
    # 此url需要从登录form的action属性中提取
    url = "http:www.renren.com/Plogin.do" 
    # 此键值需要从登录form的两个对象input中提取name属性
    data = {
        'email':'15902276147',
        'password':'123456'
    }
    #把data编码
    data = parse.urlencode(data).encode('utf-8')
    # 创建请求对象
    res = request.Request(url,data=data) 
    # 发起请求
    response = opener.open(res)

    #保存到文件
    # ignor_discard表示即使cookie将要被丢弃也要保存下来
    # ignore_expire表示如果该文件中cookie即使已经过期也要保存
    cookie.save(ignore_discard=True,ignore_expires=True)

if __name__ == '__main__':
    log_in() 



filename = 'cookie.txt' 
cookie = cookiejar.MozillaCookieJar(filename=filename)  
cookie_handle = request.HTTPCookieProcessor(cookie) 
http_handle = request.HTTPHandler() 
https_hanle = request.HTTPSHandler() 
opener = request.build_opener(http_handle,https_hanle,cookie_handle) 


def log_in(): 

    url = 'http://www.renren.com/PLogin.do' 

    data = {
        'email': '15902276147', 
        'password': 'lijinpeng'
    } 

    data = parse.urlencode(data).encode('utf-8') 

    res = request.Request(url,data=data) 

    response = opener.open(res) 

    cookie.save(ignore_discard=True,ignore_expires=True)


def get_home_page(): 

    base_url = 'http://www.renren.com/823703196/newsfeed/photo' 

    # execution log_in function,get the value of function 
    rep = opener.open(base_url).read()

    result = rep.decode('utf-8') 

    with open ('result.html','w') as f: 
        f.write(result) 
        print ('Done....')

if __name__ == '__main__': 
    log_in() 
    get_home_page()

"""

#v16.读取cookie 
"""
cookie = cookiejar.MozillaCookieJar() 
cookie.load('cookie.txt')
cookie_handle = request.HTTPCookieProcessor(cookie) 
http_handle = request.HTTPHandler() 
https_hanle = request.HTTPSHandler() 
opener = request.build_opener(http_handle,https_hanle,cookie_handle) 

def get_home_page(): 

    base_url = 'http://www.renren.com/823703196/newsfeed/photo' 

    # execution log_in function,get the value of function 
    rep = opener.open(base_url).read()

    result = rep.decode('utf-8') 

    with open ('result.html','w') as f: 
        f.write(result) 
        print ('Done....')

if __name__ == '__main__': 
    get_home_page()
""" 

# V17
"""
# 利用非认证上下文环境替换认证的上下文环境
ssl.create_default_context = ssl._create_unverified_context
url = 'https://www.12306.cn/mormhweb' 

rsp = request.urlopen(url).read() 

result = rsp.decode('utf-8') 

print (result)
"""

# v18 破解有道词典 
# 处理js加密代码 
# 通过寻找js代码中操作代码
# 这个是计算salt的公式 l = (new Date).getTime()
# 这个是计算sign的公式，md5一共需要四个参数,第一个和第四个都是固定值的字符串,第2个是salt,
# c = p.md5("new-fanyiweb" + l + "ydsecret://newfanyiweb.doctran/sign/0j9n2{3mLSN-$Lg]K4o0N2}" + a)
# a = i[i.length - 1]
# i = e * i 
"""
def youdao(key): 
    
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    data =  {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "d ict",
        "client" : "fanyideskweb",
        # salt,认为加的一个很长的字符串,为了防止黑客用使用暴力破解通过密文搜索出明文
        # 加密处理 
        "salt": "15908366612610",
        "sign": "c2250fe63d58e62c8e89e6ce36392b77",
        "ts": "1590836661261",
        "bv": "5dfabd970ef44d778884b2781249f18c",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action" :"FY_BY_REALTlME"
    }   
    # 参数data需要是bytes格式 
    data = parse.urlencode(data).encode() 

    headers = {
        "Host": "fanyi.youdao.com",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        #"Accept-Encoding":" gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": "240",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    res = request.Request(url,data=data,headers=headers) 
    rsp = request.urlopen(res) 
    result = rsp.read().decode() 
    print (result) 

if __name__ == '__main__':
    wd = 'girl'
    youdao(wd)
"""
# v19
"""
def get_salt(): 
    '''
    salt的公式: 
    l = (new Date).getTime()
    将其翻译成python代码
    '''
    import time,random

    salt= int(time.time() * 1000)

    return salt 

def get_MD5(v): 
    import hashlib 
    # 负责加密

    md5 = hashlib.md5() 
    # update需要一个bytes格式
    md5.update(v.encode('utf-8')) 
    sign = md5.hexdigest() 

    return sign 


def get_sign(key,salt) :


    sign = "new-fanyiweb" + str(salt) + "ydsecret://newfanyiweb.doctran/sign/0j9n2{3mLSN-$Lg]K4o0N2}" + a 

    sign = get_MD5(sign) 


def youdao(key):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    salt = get_salt()


    data =  {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "d ict",
        "client" : "fanyideskweb",
        # salt,认为加的一个很长的字符串,为了防止黑客用使用暴力破解通过密文搜索出明文
        # 加密处理 
        "salt": str(salt),
        "sign": get_sign(key,salt),
        "ts": "1590836661261",
        "bv": "5dfabd970ef44d778884b2781249f18c",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action" :"FY_BY_REALTlME"
    }  
    print (data) 
    # 参数data需要是bytes格式 
    data = parse.urlencode(data).encode() 

    headers = {
        "Host": "fanyi.youdao.com",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        #"Accept-Encoding":" gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    res = request.Request(url,data=data,headers=headers) 
    rsp = request.urlopen(res) 
    result = rsp.read().decode() 
    print (result) 

if __name__ == '__main__': 

    youdao('girl')
"""

# v20 
"""
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7",
    "Connection": "keep-alive",
    "Host": "movie.douban.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
    }

"""

"""
if __name__ == '__main__': 

    
    url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20'

    res = request.Request(url)
    response = request.urlopen(res)
   
    result = response.read().decode() 

    json_info = json.loads(result) 

    print (json_info) 

""" 
