#coding:utf-8 

__author__ = 'jinpeng.li' 


import socket 

"""
def client_fun(): 
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

    addr = ('127.0.0.1',8889) 

    sock.connect(addr) 

    data = sock.recv(1024).decode() 

    print (data) 

    res = 'my name is jinpeng.li' 
    response = res.encode()
    sock.send(response) 

    sec_mess = sock.recv(1024).decode() 
    print (sec_mess) 

    sock.close() 


if __name__ == '__main__': 
    client_fun() 

""" 

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

addr = ('127.0.0.1',8889) 

s.connect(addr) 

mes = s.recv(1024).decode() 
print (mes) 


name_list = [b'jinpeng.li',b'sai.hu']
for name in name_list: 
    s.send(name)
    data = s.recv(1024).decode() 
    print (data) 

msg = b'exit' 
s.send(msg) 
s.close() 

