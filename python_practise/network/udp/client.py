#coding:utf-8 
__author__ = 'jinpeng.li' 

import socket

def client_fun(): 
    # 创建实例
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    text = 'hello, my name is bob'

    # 发送的数据必须是bytes格式
    data = text.encode() 
    target_addr = ('127.0.0.1',10001)

    # sendto发送消息
    sock.sendto(data,target_addr) 
    data,addr = sock.recvfrom(1024) 
    result = data.decode() 
    print (result)

if __name__ == '__main__': 
    client_fun()



    

