# -*- coding: utf-8 -*-
from django.urls import re_path
from .views import profile_view, change_profile_view


app_name = 'oauth'

urlpatterns = [
    re_path(r'^profile/$', profile_view, name='profile'),
    re_path(r'^profile/change/$', change_profile_view, name='change_profile'),

]