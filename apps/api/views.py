# -*- coding: utf-8 -*-


from oauth.models import Ouser
from blog.models import Article, Tag, Category, Timeline
from tool.models import ToolLink
from .serializers import (UserSerializer, ArticleSerializer,
                          TimelineSerializer,TagSerializer,CategorySerializer,ToolLinkSerializer)
from rest_framework import viewsets, permissions
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


class UserListSet(viewsets.ModelViewSet):
    """用户视图集"""
    queryset = Ouser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)


class ArticleListSet(viewsets.ModelViewSet):
    """文章视图集"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TagListSet(viewsets.ModelViewSet):
    """标签视图集"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)


class CategoryListSet(viewsets.ModelViewSet):
    """分类视图集"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)


class TimelineListSet(viewsets.ModelViewSet):
    """时间线视图集"""
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)


class ToolLinkListSet(viewsets.ModelViewSet):
    """工具链接视图集"""
    queryset = ToolLink.objects.all()
    serializer_class = ToolLinkSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)