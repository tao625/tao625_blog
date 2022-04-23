# -*- coding: utf-8 -*-
# Created by dan on 2022/2/22
# Copyright (c) 2022 dan. All rights reserved.


wss = {"index":4, "bid": "12", "bdtype":"wss"}
oa = {"index":2, "bid": "2-12", "bdtype":"oa", "ports":[(1,2) ,(11, 14)]}
voa = {"index":3, "bid": "2-12", "bdtype":"voa"}
fiu = {"index":1, "bid": "2-12", "bdtype":"fiu"}
olp = {"index":5, "bid": "3-12", "bdtype":"olp"}

temp= sorted([wss, oa, voa, fiu, olp], key=lambda x:x["index"])
# print(temp)

class Func():
    def __init__(self, **kwargs):
        # for k, v in kwargs.items():
        #     setattr(self, k, v)
        self.__dict__.update(kwargs)


d = Func(**wss)
print(d.__dict__)