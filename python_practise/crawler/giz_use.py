#coding:utf-8 

from urllib import request,parse,error 
from io import BytesIO
import gzip

headers = {

    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host":"www.baidu.com",
    "User-Agent":" Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36"
}


if __name__ == '__main__': 

    url = 'https://www.baidu.com/s' 
    
    keyword = input("ple input your keyword:")

    wd = {
        'wd' : keyword
    }

    wd = parse.urlencode(wd) 

    target_url = url + '?' + wd 
    

    res = request.Request(target_url,headers=headers) 

    resposne = request.urlopen(res).read() 

    buffer = BytesIO(resposne) 

    f = gzip.GzipFile(fileobj=buffer) 

    result = f.read().decode('utf-8') 

    with open('./baidu.html','w') as f : 
        f.write(result) 

    







 
