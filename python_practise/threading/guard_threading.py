#coding:utf-8 


import time 
import threading 
"""
def fun(): 
    print ('start fun') 

    time.sleep(2) 

    print ('end fun') 

if __name__ == '__main__': 
    t = threading.Thread(target=fun,args=()) 
    t.start() 

    time.sleep(1) 
    print ('main thread end') 
""" 


def fun(): 
    print ('start fun') 

    time.sleep(2) 

    print ('end fun') 

if __name__ == '__main__': 
    t = threading.Thread(target=fun,args=()) 
    # 主线程结束,自线程也随之结束
    t.daemon = True
    t.start() 

    time.sleep(1) 
    print ('main thread end') 
