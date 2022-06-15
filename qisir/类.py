#coding:utf-8

import os

'''
创建类
'''

#
# class Person:
#     """
#     this is a sample of class
#     """
#
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def color(self, color):gggg
#         d = {}
#         d[self.name] = color
#         return d
#
#
# tom = Person('tom')  # 实例化一个对象tom
# print(tom.color('red')) # 调用实例color方法
# print(tom.get_name()) # 调用实例get_name的方法
# print(tom.name) # 实例属性name

'''
类属性

'''
class A:
    a = 9  #a 就是类A的属性

print(A.a) #A.a就是调用类属性的方式
A.yh = 20
print(A.yh)