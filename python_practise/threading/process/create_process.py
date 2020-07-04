#coding:utf-8 
import multiprocessing 
from time import sleep,time,ctime

def clock(interval): 
    while True: 
        print ('the time is %s' % ctime())
        sleep (interval) 

if __name__ == '__main__': 
    
    p = multiprocessing.Process(target=clock,args=(5,)) 
    p.start() 


