# #coding:utf-8
#
# '''
# 形参、实参定义了解
# 函数括号内的参数叫做形参
# 调用函数的时候传入的参数叫实参
# '''
# # 不定参数
# def func(x,*arg):  # 多余的参数组成一个元祖
#     print(x)
#     result = x
#     print(arg)  # 将第二个参数开始，全部塞入一个元祖中
#     for i in arg:
#         result +=i
#     return result
#
# result = func(1,2,3,4,5,6,7,8,9,10)
# print(result)
#
#
# def funb(x,**kwargs): #** 形式就是把参数当成一个字典，但是这个时候需要在传值的时候说明键和值
#     print(x)
#     print(kwargs)
#
# funb(1,a = 34, b = 56)
#
#
# def add(x,y):
#     return x+y
#
# bars = (2,3)
# print(add(*bars)) #注意的是，元组中元素的个数，要跟函数所要求的变量个数一致
'''
传递函数
将函数传入另外一个函数当参数
'''

# def bar():
#     print('i am in bar () ')
#
# def foo(func):
#     func()
#
# foo(bar)  #函数的调用,在这里是传递的是一个函数,需要注意的是传入函数的时候只需要传入函数的名字,不需要传递函数后面的()括号

# ### 举个例子
# def convert(func,seq):
#     return [func(i) for i in seq]
#
# def num(n):
#     if n %2 == 0:
#         return n**n
#     else:
#         return n*n
#
# if __name__ == '__main__':
#     myseq = (111,3.14,-56)
#     r = convert(num,myseq)  # num是一个函数
#     print(r)

'''
嵌套函数,函数不仅仅可以当参数传递,还可以在函数里面再定义一个函数, 
'''
# def foo():
#     def bar():
#         print('bar is runnging!')
#     print('foo is running')
#
# foo()
# foo().bar()  #会报错,提示foo没有对应属性,因为bar()作用于只是在函数foo内部,因此需要在foo内部进行调用

# #重新定义foo
# def foo():
#     def bar():
#         print('bar is running!')
#     bar()
#     print('foo is running')
#
# foo()  #这个时候就可以显示调用了内部的bar函数了.
##### 作用域
# def foo():
#     a = 1
#     def bar():
#         a = a+1  #此处没有对应的a变量的申明所以会报错
#         print(f'bar() a is {a}')
#     bar()
#     print(f'foo() a = {a}')
#
# foo()# 这个时候会提示a在申明前使用了

## 改造下
# def foo():
#     a = 1
#     def bar():
#         nonlocal  a
#         a = a+1  #此处没有对应的a变量的申明所以会报错
#         print(f'bar() a is {a}')
#     bar()
#     print(f'foo() a = {a}')

# foo()# 这个时候会提示a在申明前使用了会报错, 加上一个nonlocal 字段就可以了
# ---- nonlocal字段的意思是嵌套函数外,外部函数中定义的变量,要注意跟global区别

# def maker(n): # 函数的嵌套
#     def action(x):
#         return x**n
#     return  action
#
# f = maker(2) # 返回的是一个action函数对象
#
# m = f(3) #给函数对象传入参数返回的是x**n
# print(m)

'''
总结就是函数是对象,既可以当参数传递,也可以嵌套
'''
# def foo(fun):
#     def wrap():
#         print('start')
#         fun()
#         print('end')
#         print(fun.__name__)
#
#     return wrap

# def bar():
#     print('I am in bar()')
#
# f = foo(bar)
# print(f)  # 打印出来的是一个函数对象,如果需要再调用这个函数则需要加上括号
# f() # 加上括号调用函数
## 如果换一个写法如下
# @foo
# def bar():
#     print('I am in bar()')
#
# bar() # 直接调用bar函数就可以实现像上面那种写法同样的效果,这个语法叫装饰器

'''
装饰器本身是一个函数，将被装饰的类或者函数当作参数传递给装饰器函数
'''
# --------------------
'''
闭包概念
闭包是一个函数,并且具有以下的2个特点
1.定义在另外一个函数里面(嵌套函数)
2.应用其所在函数环境的自由变量
'''
# a = 3
# def foo():
#     print(a)
#
# foo()  # a =3 定义的变量在函数里面可以使用,反过来呢?
#
# def foo():
#     b = 3
#
# print (b)  # 提示b没有定义,根据作用域的关系，是合情合理的。然而，也许在某种特殊情况下，我们需要在函数外面使用函数里面的变量

# 那么我们可以像下面的写法来实现外面获取函数里面的变量
# def foo():
#     a = 3
#     def bar():
#         return a
#     return bar
#
# f = foo()
# print(f()) # 这里返回的就是变量a的值,实现了外面获取函数里面的变量
'''
在函数 	foo()	里面，有    a = 3                 	和另外一个函数 	bar()	，它们两个都在函数foo() 的环境里
它们两个是互不统属的，所以变量 	a	相对函数 bar()是自由变量，并且在函 
数 	bar()	中应用了这个自由变量——函数                     	就是我们所定义的闭包。
'''

'''
闭包函数的常用范围
'''
# 计算抛物线
# def parabola(a,b,c):
#     def para(x):
#         return  a*x**2 + b*x +c
#     return para
#
# p = parabola(2,3,4)
# print(p(5))
'''
上面的函数中parabola(a,b,c)定义了一个抛物线的函数对象——状如y	=	2x^2	+3x+4,如果要计算x=5时,只需要p(5)即可
'''
# --------------分割线-------------

'''
lambda 函数
是一个只用一行就能解决问题的函数
'''
# def add(x):
#     x += 3
#     return x
# numbers = range(10)
#
# new_numbers = []
# for i in numbers:
#     new_numbers.append(add(i))
# print(new_numbers)

# 上面实现的功能时将一个10随机内的数字,自身加3后组成一个新的list
# 如果用列表解释式则是下面的表示方法
# new_numbers = [i+3 for i in range(10)]  # 列表解析式
# print(new_numbers)

# 如果用的是lambda表达式就是这样的写法:
# lam = lambda x:x+3
# n2 = []
# numbers = range(10)
# for i in numbers:
#     n2.append(lam(i))
# print(n2)

'''
总结下lambda函数的使用方法:
1.在lambda后面直接跟变量 
2.变量后面是冒号
3.冒号后面是表达式，表达式计算结果就是本函数的返回值
'''
# lam = [lambda x:x,lambda x:x**2,lambda x:x**3,lambda x:x**4]
# for i in lam: # 遍历出来的i是一个lambda函数
#     print(i(3))
'''
map()  函数的使用方法
map(func,*iterable)
func是一个函数,*iterable 是一个序列对象.在执行的时候,序列对象中的每个元素,按照从左到右的顺序,依次被取出来,塞入到func函数里面,并将func的返回值依次存到
一个列表中
'''
# list1 = [2, 3, 5, 9, 8, 6]
# # list2 = [4, 8, 5, 7, 8, 5]
# result = map(lambda x: x + 3, list1)  # 这个lambda就是相当于函数的func入参
# print([i for i in result])

'''
例子二:
'''
# items = [1,2,3,4,5]
# square = []
# for i in items:
#     square.append(i**2)
# print(square)   # 最原始的写法

# 写法二:使用列表解析式
# items = [1,2,3,4,5]
# square = [i**2 for i in items]
# print(square)
# 写法三:使用lambda函数
# items = [1, 2, 3, 4, 5]
# suqare = lambda x: x ** 2
# new = []
# for i in items:
#     new.append(suqare(i))
# print(new)
##写法四:
# items = [1, 2, 3, 4, 5]
# square = lambda x: x ** 2
# new = map(square, items)
# print([i for i in new])
'''
理解要点:
对可迭代对象中的每个元素，依次应用function的方法（函数）（这本质上就是一个for循环）。
将所有结果返回一个列表。
如果参数很多，则对那些参数并行执行function。
'''
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [7, 8, 9, 3, 2, 1]
#
# new = map(lambda x, y: x + y, list1, list2) # 将两个列表的相同index值进行相加

# 如果有三个list,则可以继续加参数:
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [7, 8, 9, 3, 2, 1]
# list3 = [8, 9, 8, 67, 43, 23]
# new = map(lambda x, y, z: x + y + z, list1, list2, list3)  # 将两个列表的相同index值进行相加
# print([i for i in new])