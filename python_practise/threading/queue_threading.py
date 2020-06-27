#coding:utf-8 

from threading import Thread 
from time import sleep 
import queue 
"""
def count_task(items,result_queue): 
    number = 0 
    for x in items: 
        number += x
    result_queue.put(number) 

if __name__ == "__main__": 

    result_queue = queue.Queue() 
    number_list = [x for x in range(100000)]
    index = 0
    threading_list = [] 
    for _ in range(5) : 
        t = Thread(target=count_task,args=(number_list[index:index+20000],result_queue)) 
        index += 20000 
        threading_list.append(t)
        t.start() 
    
    for t in threading_list: 
        t.join() 

    result = 0 

    while not result_queue.empty(): 
        result += result_queue.get()  
    print (result)
""" 











class producer(Thread): 
    def run(self): 
        global result_queue
        counter = 0 
        while True: 
            if result_queue.qsize() < 1000: 
                for x in range(100):
                    counter = counter + 1 
                    msg = '生成产品' + str(counter) 
                    result_queue.put(msg) 
                    print (msg) 

            sleep(0.5)

class consumer(Thread): 
    def run(self): 
        global result_queue
        while True: 
            if result_queue.qsize() > 100 : 
                for x in range(3): 
                    msg = self.name + '消费了' + result_queue.get()
                    print (msg)
            sleep (1) 

if __name__ == '__main__' : 
    result_queue = queue.Queue() 
    """
    for x in range(500): 
        result_queue.put('初始产品'+str(x)) 
    """
    for x in range(2): 
        p = producer() 
        p.start() 
    
    for x in range(5): 
        c = consumer() 
        c.start()
        