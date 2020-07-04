#coding:utf-8 
__author__ = 'jinpoeng.li' 
import socket
##模拟服务器的函数
def server_fun(): 
    #1.建立socket实例
    # af_inet代表使用ipv4协议族
    # sock_dgram代表使用udp协议
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
    # 2.绑定ip地址和port 
    # 127.0.0.1代表机器本身
    # ip_address是一个tuple类型(('ip_address','port'))
    addr = ('127.0.0.1',10001)
    sock.bind(addr)

    # 3. recv client mess 
    # 等待方式为死等,没有其它的可能性
    # 用recvfrom接受的返回值是一个tuple,前一项表示数据,后一项表示地址
    # 参数的含义是缓冲区的大小
    data,addr = sock.recvfrom(1024)
    # 发送过来的数据是byte格式,必须通过解码才能得到str格式 
    # decode默认参数是utf-8
    text = data.decode()
    print (text)
    
    # 给对方返回消息
    rep = "hello,my name is jinpeng.li" 
    data = rep.encode()
    sock.sendto(data,addr) 

if __name__ == '__main__': 
    print ('starting server.............') 
    server_fun() 
    print ('ending server...........')