# -*- coding: utf-8 -*-
# Created by dan on 2022/1/7
# Copyright (c) 2022 dan. All rights reserved.
import yaml
from loguru import logger as log

# log.add('./files/ason_net.log', format="{time:YYYY-MM-DD HH:mm:ss} {level} From {module}.{function} : {message}")

path = "./files/test2.yml"
# log.info(path)

files = open(path, "r", encoding="utf-8")
files_data = files.read()
data = yaml.safe_load_all(files_data)
for d in data:
    print(d)