#coding:utf-8 

__author__ = 'jinpeng.li' 


import json 


target_dict = {'name':'jinpeng.li',
                'age':23
            } 

# 使用dump将dict写入json文件中
try : 
    with open('./jinpeng.json','w') as f : 
        json.dump(target_dict,f) 

except Exception as e : 
    print ('write json file failed!' + str(e)) 


# 用load将json文件以python格式读出
try : 
    with open('./jinpeng.json','r') as fs : 
        result = json.load(fs) 
        print (result)
        print (type(result))
except Exception as e :
    print ('read json file failed!' + str(e)) 
