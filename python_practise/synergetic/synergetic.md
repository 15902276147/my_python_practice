##########################################
#协程
-参考资料: 
http://python.jobbole.com/86481
http://python.jobbole.com/87310 


#迭代器 

-可迭代(Iterable):直接作用于for循环的变量.
-迭代器(Iterator):不但可以作用于for循环,还可以被next调用.
-list是典型的可迭代对象,但不是迭代器,不能被next调用
-iterable 和 iterator可以转换 by iter函数

#判断是否可迭代:
# from collections import Iterable,Iterator
# ll = [1,2,3,4,5] 
# print (isinstance(ll,Iterable))
# output: True 
# print (isinstance(ll.Iterator)) 
# output: False
# isinstance(判断某个变量是否是一个实例)


#iter函数: 

s = 'My name is jinpeng' 
s_iter = iter(s) 
# 此时s_iter既是可迭代对象也是迭代器. 



############################################
# 生成器 
# generator: 一边循环,一边计算下一个元素的机制/算法. 
# 需要满足三个条件: 
# 1.每次调用都生产出for循环需要的下一个元素
# 2.如果到了最后一个元素，爆出StopIteration异常
# 3.可以被next调用

如何生成一个生成器
# 直接使用生成器 
# 如果函数包含yield，则这个函数就叫生成器
# next调用函数，遇到yield返回

generator: 
L = [x * x for x in range(5)]  #放在中括号中是列表生成器
g = (x * x for x in range(5))  #放在小括号中就是生成器 
# L : list 
# g : generator 


# 生成器的实例: 
# 在生成器odd中,yiled负责返回
def odd(): 
    print ("Step 1") 
    yield 1 
    ptint ('Step 2) 
    yield 2 
    print ("Step 3) 
    yield 3 

#odd是调用生成器
g = odd() 
one = next(g) 
print (one) 

two = next(g) 
print (two)

three = next(g) 
print (three)


# for 循环调用生成器: 
def fib(max): 
    n,a,b = 0,0,1 
    while n < max : 
        print (b) 
        a,b = b,a+b 
        n += 1 
    return None 
fib(5) 

# 斐波那契数列的生成器写法 
def fib(max): 
    n,a,b = 0,0,1 
    while n < max: 
        yield b 
        a,b = b ,a+b 
        n += 1 
    需要注意的是,爆出异常的返回值是return的返回值
    return None 

g = fib(5) 

for x in range(6): 
    rst = next(g) 
    print (rst) 



























