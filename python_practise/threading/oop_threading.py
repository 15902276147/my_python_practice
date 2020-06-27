#coding:utf-8

import threading 
import time 


# 类需要继承自threading.Thread 
class MYTHREAD(threading.Thread): 
    def __init__(self,arg): 
        super(MYTHREAD,self).__init__() 
        self.arg = arg 
    
    # 必须重写run函数,run函数代表的是真正执行的功能
    def run(self): 
        time.sleep(2) 
        print ('the args for this class is {0}'.format(self.arg))


for x in range(5): 
    t = MYTHREAD(x) 
    t.start() 
    t.join() 

print ('Main thread is done!!!')