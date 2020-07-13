# coding:utf-8

from collections import Iterator,Iterable


def fib(max): 
    n,a,b = 0,0,1 
    while n < max: 
        yield b 
        a,b = b,a+b 
        n += 1 
    return 'Done'
"""
g = fib(5) 

for x in range(6): 
    res = next(g) 
    print (res)
"""

ge  = fib(10) 
for x in ge: 
    # 生成器的典型用法是在for中使用
    # 比较常用的典型生成器是range
    print (x)

"""
1
1
2
3
5
Traceback (most recent call last):
  File "iter.py", line 14, in <module>
    res = next(g) 
StopIteration: Done
"""

"""
def odd(): 
    print ('Step 1') 
    yield 1 
    print ('Step 2 ') 
    yield 2 
    print ('Step 3 ') 
    yield 3 

g = odd() 
n = odd()
 
for x in range (3): 
    res = next(g)
    if x  == 2 : 
        print (res)

for y in range(3): 
    res = next(n) 
    print (res)

"""

"""
L = [x for x in range(5)] 
print (type(L)) 

g = (x for x in range(3)) 

if isinstance(L,Iterator): 
    for x in L : 
        print (x) 
else: 
    s_iter = iter(L) 
    for _ in range(5): 
        res = next(s_iter) 
        print (res) 
"""


