# -*- coding: utf-8 -*-
from oauth.models import Ouser
from rest_framework import serializers
from blog.models import Article, Tag, Category, Timeline
from tool.models import ToolLink, ToolCategory


class UserSerializer(serializers.ModelSerializer):
    """用户序列化器"""
    class Meta:
        model = Ouser
        fields = ('id', 'username', 'first_name', 'link', 'avatar')


class TagSerializer(serializers.ModelSerializer):
    """标签序列化器"""
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """分类序列化器"""
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    """文章序列化器"""
    author = serializers.ReadOnlyField(source='author.username')
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    keywords = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Article
        exclude = ('body',)


class TimelineSerializer(serializers.ModelSerializer):
    """时间线序列化器"""
    class Meta:
        model = Timeline
        fields = '__all__'


class ToolCategorySerializer(serializers.ModelSerializer):
    """工具分类序列化器"""
    class Meta:
        model = ToolCategory
        fields = '__all__'


class ToolLinkSerializer(serializers.ModelSerializer):
    """工具链接序列化器"""
    category = ToolCategorySerializer()

    class Meta:
        model = ToolLink
        fields = '__all__'
