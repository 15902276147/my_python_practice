#coding:utf-8 
from threading import Thread,Lock
from time import sleep 
lock_1 = Lock() 
lock_2 = Lock() 
def fun_1(): 
    
    print ("func_1 starting.....") 

    lock_1.acquire() 
    
    print ('func_1 申请了lock_1......') 

    sleep(2) 

    print ('func_1 等待lock_2...')

    lock_2.acquire() 
    print ('func_2申请了 lock_2.....') 

    lock_2.release() 

    print ('func_1 释放了lock_2') 
    lock_1.release() 

    print("func_1释放了lock_1") 

    print ('func_1 done...... ') 

def fun_2(): 

    print ("fun_2 starting......") 
    lock_2.acquire() 
    print('func_2申请了lock_2.....')
    sleep(4) 
    print ('func_2等待lock_1.....') 
    lock_1.acquire() 
    print ('fun_2申请了lock_1....')
    lock_1.release() 

    print ('lock_2释放了lock_1...') 

    lock_2.release() 
    print('lock_2释放了lock_2.....') 

    print ('func_2 done......') 

if __name__ == '__main__': 

    print ('主程序启动') 

    t1 = Thread(target=fun_1,args=())
    t2 = Thread(target=fun_2,args=())
    t1.start() 
    t2.start() 
    t1.join() 
    t2.join() 
    print ('主程序启动.......')