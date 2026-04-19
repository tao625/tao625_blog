# -*- coding: utf-8 -*-
from django.urls import re_path
from .views import (Toolview, BD_pushview, BD_pushview_site,
                    regexview, useragent_view, html_characters,
                    docker_search_view,
                    )

app_name = 'tool'

urlpatterns = [
    re_path(r'^$', Toolview, name='total'),  # 工具汇总页
    re_path(r'^baidu-linksubmit/$', BD_pushview, name='baidu_push'),  # 百度主动推送
    re_path(r'^baidu-linksubmit-sitemap/$', BD_pushview_site, name='baidu_push_site'),  # 百度主动推送 sitemap
    re_path(r'^regex/$', regexview, name='regex'),  # 正则表达式在线
    re_path(r'^user-agent/$', useragent_view, name='useragent'),  # user-agent 生成器
    re_path(r'^html-special-characters/$', html_characters, name='html_characters'),  # HTML 特殊字符查询
    re_path(r'^docker-search/$', docker_search_view, name='docker_search'),  #docker 镜像查询
]
