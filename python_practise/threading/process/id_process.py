#coding:utf-8 

import os 
import multiprocessing 


def info(title): 
    print (title) 
    print ('module name:' + __name__) 
    #得到父进程的pid 
    print ('parent process:', os.getppid()) 
    # 得到本身进程的id
    print ('process id:' ,os.getpid())

def f (name): 
    info('function f') 
    print ('hello',name) 

if __name__ == '__main__': 
    info ('main line') 
    p = multiprocessing.Process(target=f,args=('bob',)) 
    p.start() 
    p.join()

"""

main line
module name:__main__
parent process: 60048
process id: 60546
function f
module name:__main__
parent process: 60546
process id: 60547
hello bob

"""