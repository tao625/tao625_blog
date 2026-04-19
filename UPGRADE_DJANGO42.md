# Django 4.2 升级指南

本项目已从 Django 1.11 升级到 Django 4.2 LTS 版本。本文档说明了所有重要的变更和升级步骤。

## 主要变更

### 1. 依赖包更新

**核心框架:**
- Django: 1.11.12 → 4.2.29
- djangorestframework: 3.8.2 → 3.15.2
- django-allauth: 0.33.0 → 0.63.6

**数据库和缓存:**
- PyMySQL: 0.7.11 → 1.1.1
- django-redis: 4.9.0 → 5.4.0
- redis: 2.10.6 → 5.0.1

**前端相关:**
- django-crispy-forms: 1.6.1 → 2.1
- 新增：crispy-bootstrap4==2024.1 (Django 4.2 需要)
- django-imagekit: 4.0.1 → 5.0.0
- Pillow: 6.2.0 → 10.4.0

**搜索:**
- django-haystack: 2.7.0 → 3.3.0
- jieba: 0.39 → 0.42.1

**其他:**
- Markdown: 2.6.8 → 3.6
- Pygments: 2.2.0 → 2.18.0
- bleach: 2.1.1 → 6.1.0
- gunicorn: 19.7.1 → 22.0.0

### 2. Settings.py 配置变更

#### 移除的组件:
```python
# 移除 bootstrap_admin (不再兼容)
'bootstrap_admin',
```

#### 新增的组件:
```python
# 添加 crispy-bootstrap4 支持
'crispy_bootstrap4',

# allauth 中间件 (Django 4.2 必需)
'allauth.account.middleware.AccountMiddleware',
```

#### 新增的安全配置:
```python
# Django 4.2 新增安全设置
CSRF_TRUSTED_ORIGINS = os.getenv('IZONE_CSRF_TRUSTED_ORIGINS', '').split(',') if os.getenv('IZONE_CSRF_TRUSTED_ORIGINS') else []
```

#### 表单配置更新:
```python
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap4'
```

#### REST Framework 配置更新:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
}
```

### 3. URL 配置变更

所有 URL 配置从 `url()` 迁移到 `re_path()`:

**之前 (Django 1.11):**
```python
from django.conf.urls import url

urlpatterns = [
    url(r'^article/(?P<slug>[\w-]+)/$', DetailView.as_view(), name='detail'),
]
```

**现在 (Django 4.2):**
```python
from django.urls import re_path

urlpatterns = [
    re_path(r'^article/(?P<slug>[\w-]+)/$', DetailView.as_view(), name='detail'),
]
```

**所有 URL 模块都添加了 `app_name` 命名空间:**
```python
app_name = 'blog'  # 或其他应用名称
```

### 4. Models.py 变更

所有 ForeignKey 和 ManyToManyField 都添加了 `on_delete` 参数:

```python
# Django 1.11 (已废弃)
author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者')

# Django 4.2 (必需)
author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)
```

### 5. 模板系统变更

#### 文档字符串更新:
所有文档字符串从单引号改为双引号，符合 PEP 8 规范:

```python
# 之前
'''这是文档字符串'''

# 现在
"""这是文档字符串"""
```

#### 字符串格式化:
使用 f-string 替代旧的格式化方式:

```python
# 之前
return '{}://{}'.format(protocol, domain)

# 现在
return f'{protocol}://{domain}'
```

### 6. 移除的 Django 功能

- `USE_L10N` 设置在 Django 4.2 中已废弃，已移除
- `django.conf.urls.url` 已废弃，使用 `django.urls.re_path` 替代
- `bootstrap_admin` 不再兼容，已移除

## 升级步骤

### 1. 安装新依赖

```bash
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

### 2. 数据库迁移

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. 更新静态文件

```bash
python manage.py collectstatic
```

### 4. 测试运行

```bash
python manage.py runserver
```

访问 http://localhost:8000/ 测试网站功能。

## 已知的兼容性问题

### 1. Haystack 搜索

Haystack 3.x 与 Django 4.2 完全兼容，但 `whoosh_cn_backend.py` 中的一些代码可能需要更新：

- 移除 `django.utils.six` 的使用 (Django 4.2 已移除)
- 移除 `django.utils.datetime_safe` 的使用
- 更新 `force_text` 为 `force_str`

### 2. Allauth

Django-allauth 0.63.6 需要添加中间件:

```python
MIDDLEWARE = [
    # ... 其他中间件
    'allauth.account.middleware.AccountMiddleware',
]
```

### 3. Crispy Forms

需要单独安装 `crispy-bootstrap4`:

```bash
pip install crispy-bootstrap4==2024.1
```

并在 settings.py 中添加:

```python
INSTALLED_APPS = [
    # ...
    'crispy_forms',
    'crispy_bootstrap4',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap4'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
```

## 性能优化建议

1. **数据库查询优化**: 已在主要视图中添加 `select_related` 和 `prefetch_related`
2. **缓存配置**: 使用 Redis 缓存，配置已更新
3. **静态文件**: 建议使用 CDN 或 WhiteNoise 处理静态文件

## 安全建议

1. **生产环境设置**: 
   - 设置 `DEBUG = False`
   - 配置正确的 `ALLOWED_HOSTS`
   - 启用 `SECURE_SSL_REDIRECT`

2. **密钥管理**: 
   - 使用环境变量管理 `SECRET_KEY`
   - 不要将敏感信息提交到版本控制

3. **CSRF 保护**:
   - 配置 `CSRF_TRUSTED_ORIGINS`
   - 启用 `CSRF_COOKIE_SECURE`

## 故障排除

### 问题 1: 导入错误 `No module named 'django.utils.six'`

**解决方案**: Django 4.2 移除了 six 库，需要更新相关代码:
```python
# 替换
from django.utils import six
# 为
import six
```

### 问题 2: Allauth 登录错误

**解决方案**: 确保添加了 allauth 中间件:
```python
'allauth.account.middleware.AccountMiddleware',
```

### 问题 3: 静态文件不显示

**解决方案**: 
```bash
python manage.py collectstatic --noinput
```

检查 settings.py 中的 STATIC_ROOT 和 STATIC_URL 配置。

## 参考资源

- [Django 4.2 官方文档](https://docs.djangoproject.com/en/4.2/)
- [Django 升级指南](https://docs.djangoproject.com/en/4.2/releases/4.2/)
- [django-allauth 文档](https://django-allauth.readthedocs.io/)
- [DRF 3.15 文档](https://www.django-rest-framework.org/)

## 后续计划

1. 考虑升级到 Python 3.10+ 以获得更好的性能
2. 添加异步任务支持 (Celery)
3. 使用 Django Channels 添加 WebSocket 支持
4. 添加单元测试覆盖率

---

**升级日期**: 2024
**升级版本**: Django 1.11 → Django 4.2
