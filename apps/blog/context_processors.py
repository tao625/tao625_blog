# -*- coding: utf-8 -*-

from django.conf import settings
from .utils import site_full_url


# 自定义上下文管理器
def settings_info(request):
    return {
        'site_end_title': settings.SITE_END_TITLE,
        'web_name':settings.WEB_NAME,
        'site_description': settings.SITE_DESCRIPTION,
        'site_keywords': settings.SITE_KEYWORDS,
        'tool_flag': settings.TOOL_FLAG,
        'api_flag': settings.API_FLAG,
        'cnzz_protocol': settings.CNZZ_PROTOCOL,
        'beian': settings.BEIAN,
        'my_github': settings.MY_GITHUB,
        'site_verification': settings.MY_SITE_VERIFICATION,
        'site_url': site_full_url(),
        'hao_flag': settings.HAO_FLAG,
        'hao_web_url': settings.HAO_WEB_URL,
        'jupyter_notebook_url': settings.JUPYTER_NOTEBOOK_URL
    }
