# -*- coding: utf-8 -*-
from django.urls import path, re_path
from .views import (IndexView, DetailView, CategoryView, TagView, AboutView,
                    SilianView, MySearchView, ArchiveView, TimelineView)

app_name = 'blog'

urlpatterns = [
    # path(r'^go/$', goview, name='go'),  # 测试用页面

    re_path(r'^$', IndexView.as_view(), name='index'),  # 主页，自然排序
    re_path(r'^hot/$', IndexView.as_view(), {'sort': 'v'}, name='index_hot'),  # 主页，按照浏览量排序
    re_path(r'^article/(?P<slug>[\w-]+)/$', DetailView.as_view(), name='detail'),  # 文章内容页
    re_path(r'^category/(?P<slug>[\w-]+)/$', CategoryView.as_view(), name='category'),
    re_path(r'^category/(?P<slug>[\w-]+)/hot/$', CategoryView.as_view(), {'sort': 'v'},
            name='category_hot'),
    re_path(r'^tag/(?P<slug>[\w-]+)/$', TagView.as_view(), name='tag'),
    re_path(r'^tag/(?P<slug>[\w-]+)/hot/$', TagView.as_view(), {'sort': 'v'}, name='tag_hot'),
    re_path(r'^about/$', AboutView, name='about'),  # About 页面
    re_path(r'^timeline/$', TimelineView.as_view(), name='timeline'),  # timeline 页面
    re_path(r'^archive/$', ArchiveView.as_view(), name='archive'),  # 归档页面
    re_path(r'^silian\.xml$', SilianView.as_view(content_type='application/xml'), name='silian'),  # 死链页面
    re_path(r'^search/$', MySearchView.as_view(), name='search_view'),  # 全文搜索
]
