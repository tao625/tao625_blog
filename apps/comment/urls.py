# -*- coding: utf-8 -*-
from django.urls import re_path
from .views import AddcommentView, NotificationView, mark_to_read, mark_to_delete

app_name = 'comment'

urlpatterns = [
    re_path(r'^add/$', AddcommentView, name='add_comment'),
    re_path(r'^notification/$', NotificationView, name='notification'),
    re_path(r'^notification/no-read/$', NotificationView, {'is_read': 'false'}, name='notification_no_read'),
    re_path(r'^notification/mark-to-read/$', mark_to_read, name='mark_to_read'),
    re_path(r'^notification/mark-to-delete/$', mark_to_delete, name='mark_to_delete'),
]
