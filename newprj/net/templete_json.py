# -*- coding: utf-8 -*-
# Created by dan on 2022/1/8
# Copyright (c) 2022 dan. All rights reserved.
import json
from string import Template

data = {
    "name": "dan",
    "ip": "$ip"
}

# class MyTemplete(Template):
#
#     delimiter = "#"

path = "./files/temple.json"
# with open(path, "w", encoding="utf-8") as f:
#     json.dump(data, f, indent=4)



with open(path, "r") as f:
    tp = Template(f.read())
    tp.delimiter = "#"
    print(tp.delimiter)

    # print(tp.substitute(ip="123.1.2.3.4"))
    print(tp.safe_substitute(ip="123.1.2.3.4"))