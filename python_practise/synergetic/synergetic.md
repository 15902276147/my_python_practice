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


# 协程 
- 历史历程 
- 用yield实现 
- 实现的协程比较好的包有asyncio,tornado.gevent 
- 协程: 是为非抢占多任务产生子程序的计算机程序组件,协程允许不同入口点
在不同位置暂停或开始执行程序
- 从技术角度讲,协程是一个可以暂停执行的函数,或者干脆把协程理解成生成器

- 协程的实现：
1.yield返回
2.send调用

# 协程的四个状态: 
# inspect.getgeneratorstate(...)函数确定,该函数会返回下述字符串中的一个:
1.GEN_CREATED:等待开始执行
2.GEN_RUNNING:解释器正在执行
3.GEN_SUSPENED:在yield表达式处暂停
4.GEN_CLOSED:执行结束
-next预激(prime)

# 协程终止
1. 协程中未处理的异常会向上冒泡,传给next函数或send方法的调用力(
     即触发协程的对象
 ) 
2. 终止写成的一种方式,发送莫哥哨符值，让协程退出,内置的None和Ellipsis等
常量经常用作哨符值==。

# yield from
1.调用协程为了得到返回值，协程必须正常终止
2.生成器正常终止会发出StopIteration异常,异常对象的value属性保存返回值
3.yield from 从内部捕获StopIteration异常
4.委派生成器: 
    - 包含yield from 表达式的生成器函数 
    - 委派生成器在yield from表达式出暂停,调用方可以直接把数据发给子生成器,
    子生成器把产出的值发送给调用方
    -子生成器在最后,解释器会抛出StopIteration,并把返回值附加在异常对象上





















