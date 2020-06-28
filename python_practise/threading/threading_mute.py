#coding :utf-8

import threading 
import time 


class MyThread(threading.Thread): 

    def run(self): 
        global num 
        time.sleep(1) 

        if mutex.acquire(1): 
            num = num + 1 
            mes = self.name + 'set name to ' + str(num) 
            print (mes) 
            mutex.acquire() 
            mutex.release() 
            mutex.release() 

num = 0 

mutex = threading.RLock() 

def fun_c (): 
    for x in range(5): 
        t = MyThread() 
        t.start() 
if __name__ ==  '__main__': 
    fun_c() 