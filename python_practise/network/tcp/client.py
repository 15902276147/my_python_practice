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


def client_fun(): 
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

    addr = ('127.0.0.1',8983) 

    sock.connect(addr) 

    first_recv_mess = sock.recv(1024).decode() 
    print (first_recv_mess) 

    name_list = [b'jinpeng.li',b'sai.hu',b'jinli.lin'] 

    for name in name_list: 
        sock.send(name) 
        second_recv_mess = sock.recv(1024).decode() 
        print (second_recv_mess)  

    fin_mess = b'exit' 
    sock.send(fin_mess)
    sock.close() 

if __name__ == '__main__': 
    client_fun()


