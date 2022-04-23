# -*- coding: utf-8 -*-
# Created by dan on 2022/1/9
# Copyright (c) 2022 dan. All rights reserved.
"""
python 内置函数
"""
import math
import random
import site

li = ["a", 1, 2, 5]
msg = "abcd123中国$"


def func():
    pass


print(ascii(msg))
print(f"{71:#0}")

print(bytes(msg, encoding="gbk"))
print(bytes([1, 5]))
print(callable(msg))
print(callable(func))
print(chr(97))
print(ord("a"))
print("==" * 30)


class A:
    name = "dan"

    @classmethod
    def print_name(self):
        """print name

        :return:
        """
        print("name A")

    def get_print_age(self):
        print("age")


a = A()
a.print_name()
A.print_name()
print(a.__class__.__qualname__)
print(func.__module__)
print(A.__module__)
print("==" * 30)

c = compile("for i in range(3):print(i)", mode="exec", filename="")
eval(c)
print(dir())
print(dir(a.name))
print(divmod(8.2, 2))
name = "dan"
eval("print(f'my {name}')")
exec("print(f'my is {name}')")
print(eval("1+1"))
print(exec("1+1"))
f = frozenset("abc")
print("^^" * 30)
data = {"a": 1, "b": 1.00}
# if hash(data['a']) == hash(data["b"]):
#     print("===")
if data["a"] == data["b"]:
    print("====")
# age = input("age:")
# print(age)

print(isinstance(name, (bool, int)))
print(issubclass(A, object))
with open("comp.txt", "r") as f:
    for block in iter(f.readlines()):
        print(block, file=open("test2.txt", "a"))
print(sorted([1, 3, 2, 5, 4], reverse=True))
print(sorted([{"age": 12}, {"age": 14}, {"age": 13}], key=lambda x: x["age"]))
print("my name is dan", sep="#")


def get_sum():
    print("1+1=", 2)


class B():
    """Bfafafaa

    """
    get_sum = staticmethod(get_sum)

    def __init__(self, name):
        self.name = name

    def get_name(self):
        """中国"""
        print("print_name...")
        return ""

    def set112_name(self, value):
        print("set_name..")

    def del_name(self):
        print("del_name")

    # x = property(get_name, set112_name, del_name)


print("9090")
b = B("dan122")
print(b.__repr__)
print("".join(reversed("abchfg")))
b.get_sum()

C = type("C", (A,), dict(hobby="football"))
c  = C()
print(c.hobby)
print(dict(sex="male", num=10))
print(vars(B))
print(vars(b))
print(vars())
print(locals())
print(globals())
import itertools
x1 = [1,2,3,5,6,78]
y1 = ["a", "b", "c", "d"]
x2, y2 = zip(*itertools.zip_longest(x1, y1, fillvalue=0))
print(x2, y2)
print(site.PREFIXES)
print(site.USER_SITE)
print(site.USER_BASE)
print(site.ENABLE_USER_SITE)
print(site.getsitepackages())
print("##"*30)
print(credits())
print(math.floor(3.6))
print(math.ceil(3.6))
msg = msg.join(["name$$", "56"])
print(msg)
import os
print(os.path.join(os.path.dirname(__file__), "aaa.txt"))
print((1,2,3,4,)[:2])
print(msg.encode())

for i in range(len(li)):
    print("i", i)
    print(li[i])

print(random.randint(1,2))
print("***"*10)
print(os.path.splitext(os.path.abspath(__file__)))
print(os.listdir(os.path.dirname(__file__)))