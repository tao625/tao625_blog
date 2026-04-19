# 似水年华

一个基于 Django 搭建的个人博客，采用现代化的卡片式设计。

## 功能特点

- 文章发布与管理（支持 Markdown）
- 分类与标签系统
- 评论与消息通知
- 用户注册登录（支持社交账号登录）
- 友链管理
- 响应式设计，适配移动端

## 技术栈

- **后端**：Django 4.2
- **前端**：Bootstrap 4 + 原生 CSS
- **数据库**：SQLite（默认）
- **社交登录**：django-allauth

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/tao625/tao625_blog.git
cd tao625_blog
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 数据库初始化

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4. 运行开发服务器

```bash
python manage.py runserver
```

访问 http://127.0.0.1:8000 查看博客首页。

## 项目结构

```
tao625_blog/
├── apps/
│   └── blog/              # 博客应用
│       ├── models.py       # 数据模型
│       ├── views.py       # 视图函数
│       ├── urls.py         # URL 配置
│       ├── admin.py        # 管理后台
│       └── templates/      # 模板文件
├── templates/              # 账户相关模板
├── izone/                  # Django 项目配置
├── manage.py
└── requirements.txt
```

## 界面预览

博客采用现代化的卡片式布局：

- 左侧窄边栏导航（首页、归档、工具、关于）
- 中间文章卡片列表
- 右侧边栏（用户卡片、分类、标签、友链）

## License

MIT License
