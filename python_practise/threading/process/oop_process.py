#coding:utf-8 

import multiprocessing 
from time import sleep,time 

class ClockProcee(multiprocessing.Process): 
    """
    两个函数比较重要
    1.init函数
    2.run函数 
    """
    def __init__(self,interval): 
        super().__init__() #调用父类的构造函数
        self.interval = interval 
    
    def run(self): 
        while True: 
            print ("the time is %s" % time()) 
            sleep(self.interval) 

if __name__ == '__main__': 
    p = ClockProcee(3) 
    p.start() 
        