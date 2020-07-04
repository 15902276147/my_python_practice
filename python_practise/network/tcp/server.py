#coding:utf-8

__author__ = 'jinpeng.li'


import socket 
from threading import Thread
from time import sleep
"""
def tcp_fun(): 
    # 建立socket负责具体通信,这个socket其实只负责接收对方的请求，真正通信的是链接后需要的两个参数
    # sock_stream代表使用tcp进行通讯

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    addr = ("127.0.0.1",8889) 
    sock.bind(addr) 

    # 监听接入访问socket 
    # listen(n) n 代表 服务器拒绝连接之前,操作系统可以挂起的最大连接数, ----》 排队的数量
    # n + 服务器正在处理的socket连接数 = socket允许的最大连接数
    sock.listen(3) 

    while True : 
        # 接收一个连接
        # accept返回的tupl类型内容,tuple分两部分,第一部分是str，另一是port
        s,addr  = sock.accept() 
        s.send(b'welcome connect................')
        # 每次最多接收1k字节:
        msg  = s.recv(1024) 
        # 接收到的data需要编码 
        msg.decode() 

        res = 'received msg:{0} from {1}'.format(msg,addr) 
        data = res.encode()
        s.send(data)

        s.close() 

if __name__ == '__main__': 

    print ('starting server.....') 
    tcp_fun() 
    print ('ending server........')

"""


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

add = ('127.0.0.1',8889) 

s.bind(add) 

s.listen(5) 

print ('waiting for connect........') 


def server_fun(sock,addr): 

    print ('accept new connection from %s:%s.......' % addr) 

    sock.send(b'welcome connection......') 

    while True: 
        data = sock.recv(1024).decode() 
        sleep(1)
        if not data or data == 'exit': 
            break 
            
        mesg = ('hello %s' % data).encode() 
        sock.send(mesg) 
    
    sock.close() 
    print ('connection will closed from %s:%s' % addr) 

if __name__ == '__main__': 
    
    while True: 
        sock,addr = s.accept() 

        t = Thread(target=server_fun,args=(sock,addr)) 
        t.start() 
