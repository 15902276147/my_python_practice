#coding:utf-8 
"""
def simple_coroutine(): 
    print ('---> start') 
    
    x = yield 

    print ('---> recived',x) 


sc = simple_coroutine() 

print (1111) 

#可以使用sc.send(None)，效果一样
#预激
#next(sc) 
sc.send(None)

print (2222) 
#给x赋值
sc.send('zhexiao')
"""


"""
def simple_coroutine(a): 
    print ('---> start') 

    b = yield a 
    print ('--->recived',a,b) 

    c = yield a + b 

    print ('---> rexcived',a,b,c) 

    d = yield a+b+c

# runc
sc = simple_coroutine(5) 

aa = next(sc) 
print (aa) 

bb = sc.send(6) 
print (bb)

cc = sc.send(7) 
print (cc)

""" 



#yield from 

def gen():
    for c in 'AB' : 
        yield c  
    
    #list直接用生成器作为参数 
print (list(gen())) 

def gen_new(): 
    yield from 'AB' 

print (list(gen_new()))

