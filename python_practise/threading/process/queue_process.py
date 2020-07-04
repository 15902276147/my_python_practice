#coding:utf-8 

import multiprocessing 
from time import ctime 


def consumer(input_q): 
    print ('Into consumer:',ctime()) 

    while True: 
        # 处理项 
        item = input_q.get() 
        if item is None: 
            break 
        print ('pull',item,'out of q') #此处替换为有用的工作
        input_q.task_done() #发出信号通知任务完成
    print ('Out of consumer:',ctime()) 


def producer(sequence,output_q): 
    print ('Into procuder:',ctime()) 
    for item in sequence: 
        output_q.put(item) 
        print ('put',item,'into_q') 

    print ('Out of producer:',ctime()) 

# create process 
if __name__ == '__main__': 

    # 创建Queue实例
    q = multiprocessing.JoinableQueue() 
    # 运行消费者进程 
    cons_p = multiprocessing.Process(target=consumer,args=(q,)) 
    cons_p.daemon = True 
    # 进程在主进程结束的时候自动退出
    cons_p.start() 

    # 生产多个项,sequence代表要发送给消费者的项序列 
    # 在实践中,这可能是生成器的输出活通过一些其它方式生产出来 
    sequence = [1,2,3,4,None] 
    producer(sequence,q) 
    
    q.join() 

"""
Into procuder: Sun Jul  5 00:07:25 2020
put 1 into_q
put 2 into_q
put 3 into_q
put 4 into_q
Out of producer: Sun Jul  5 00:07:25 2020
Into consumer: Sun Jul  5 00:07:25 2020
pull 1 out of q
pull 2 out of q
pull 3 out of q
pull 4 out of q
"""


