#coding:utf-8 

import threading 
"""
sum = 0 
loop_sum = 10000000 

def my_add(): 
    global loop_sum , sum
    for x in range(1,loop_sum): 
        sum += 1 
    print (sum)

def myminu(): 
    global loop_sum , sum

    for x in range(1,loop_sum): 
        sum -=1 
    print (sum)
if __name__ == '__main__': 
    my_add() 
    myminu()
"""

# use threading but no lock 
"""
sum = 0 
loop_sum = 10000000 

def my_add(): 
    global loop_sum , sum
    for x in range(1,loop_sum): 
        sum += 1 
    print (sum)

def myminu(): 
    global loop_sum , sum

    for x in range(1,loop_sum): 
        sum -=1 
    print (sum)

if __name__ == '__main__': 
    print ('starting .....{0}'.format(sum)) 

    t1 = threading.Thread(target=my_add,args=()) 
    t2 = threading.Thread(target=myminu,args=()) 

    t1.start() 
    t2.start()
    t1.join() 
    t2.join() 
""" 

# use lock: 

sum = 0 

loop_sum = 10000000 

lock = threading.Lock() 

def my_add(): 
    global sum,loop_sum 
    
    for x in range (1,loop_sum): 
        # 上锁
        lock.acquire() 
        sum += 1 
        lock.release() 
    print (sum) 

def my_minu(): 
    global sum,loop_sum 
    for y in range(1,loop_sum): 
        lock.acquire() 
        sum -= 1 
        lock.release() 
    print (sum) 

if __name__ == '__main__': 
    print ('starting.....{0}'.format(sum)) 
    t1 = threading.Thread(target=my_add,args=()) 
    t2 = threading.Thread(target=my_minu,args=()) 
    t1.start() 
    t2.start()
    t1.join()
    t2.join() 
    print ('ending.....{0}'.format(sum))