#coding :utf-8 

import threading 

import time 

# 参数定义最多几个线程同时使用资源
semaphore = threading.Semaphore(3) 

def fun_c(): 

    if semaphore.acquire(): 
        for x in range(5): 
            print (threading.current_thread().getName()+'get semaphore') 
    
    time.sleep(5) 
    semaphore.release() 

    print (threading.current_thread().getName() + 'release semaphore')


for y in range(8): 
    t = threading.Thread(target=fun_c,args=()) 

    t.start() 