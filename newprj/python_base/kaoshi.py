# -*- coding: utf-8 -*-
# Created by dan on 2022/2/11
# Copyright (c) 2022 dan. All rights reserved.
import re

str1 = """Why my age is 
          hfjahfj 123, hfajfa"""

obj = re.match('^Why.*?(\d+).*', str1, re.DOTALL)

if obj:
    print(obj.group(1))