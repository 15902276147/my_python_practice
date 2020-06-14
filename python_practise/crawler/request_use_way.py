 #coding:utf-8 

__author__ = 'jinpeng.li' 


import requests 

# v1 get方法 
"""
url = 'https://www.baidu.com' 
"""
"""
res = requests.get(url) 
print (res.text)

resp = requests.request('get',url=url) 
print (resp.text)
""" 

# v2 GET
"""
url = 'https://www.baidu.com/s?' 

kw = {
    'wd' :'NBA'
} 

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'

}

res = requests.get(url,params=kw,headers=headers) 

#print (res.text) 
#print (res.status_code) 
#print (res.content) 
#print (res.url) 
#print (res.encoding)

""" 

# v3. post 


base_url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

#存放用来模拟form的数据一定是dict格式(硬性规定)
data = {
    #girl是翻译输入的英文内容,应该是由用户输入,此处硬编码
    'kw' : 'girl'     
}

headers = {
    
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7",
    "Connection": "keep-alive",
    "Content-Length": str(len(data)),
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "fanyi.youdao.com",
    "Origin": "http://fanyi.youdao.com",
    "Referer": "http://fanyi.youdao.com/",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

rsp = requests.post(url=base_url,data=data,headers=headers) 

print (rsp.text) 





