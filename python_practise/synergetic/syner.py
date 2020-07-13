#coding:utf-8 



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