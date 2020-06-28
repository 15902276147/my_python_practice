#coding:utf-8 

import threading 
import time 

def fun_c(): 
    print ('i am running.....') 
    time.sleep(4) 
    print ('i am done....') 



if __name__ == '__main__': 
    t = threading.Timer(6,fun_c) 
    t.start() 

    i = 0 
    while True : 
        print ('%d *************' % i) 
        time.sleep(1) 
        i += 1