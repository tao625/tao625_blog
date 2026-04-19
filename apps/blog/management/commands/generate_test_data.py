from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from blog.models import Category, Tag, Article, FriendLink
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Generate test data for blog'

    def handle(self, *args, **options):
        User = get_user_model()

        # Get or create test user
        user, _ = User.objects.get_or_create(
            username='tao625',
            defaults={'is_staff': True, 'is_superuser': True}
        )

        # Create categories
        categories_data = ['Python', 'Django', 'JavaScript', 'Frontend', 'Backend', 'DevOps', 'Tools', 'Life']
        categories = []
        for name in categories_data:
            cat, _ = Category.objects.get_or_create(
                name=name,
                slug=name.lower()
            )
            categories.append(cat)
        self.stdout.write(f'Created {len(categories)} categories')

        # Create tags
        tags_data = ['Django', 'RESTful', 'Vue', 'React', 'CSS', 'Docker', 'Git', 'Linux', 'Nginx', 'Redis', 'MySQL', 'Algorithm', 'Interview', 'Tips']
        tags = []
        for name in tags_data:
            tag, _ = Tag.objects.get_or_create(
                name=name,
                slug=name.lower()
            )
            tags.append(tag)
        self.stdout.write(f'Created {len(tags)} tags')

        # Create articles
        article_titles = [
            'Django REST Framework Complete Guide',
            'Docker Django Application Deployment',
            'JavaScript ES6+ New Features',
            'CSS Grid Layout Tutorial',
            'Git Advanced Tips and Workflow',
            'Python Async Programming',
            'Vue 3 Composition API Guide',
            'Nginx Performance Optimization',
            'Redis Cache Best Practices',
            'Programmer Interview Experience',
            'MySQL Index Optimization',
            'Linux Server Security',
            'React Hooks Guide',
            'Django ORM Performance Tips',
            'Frontend Backend Separation Architecture',
        ]

        body_template = 'This is a detailed technical tutorial covering core knowledge points and practical experience. By learning this article, you will master key technical concepts and best practices.'

        for i, title in enumerate(article_titles):
            category = random.choice(categories)
            article_tags = random.sample(tags, random.randint(2, 4))
            days_ago = random.randint(1, 180)
            create_date = datetime.now() - timedelta(days=days_ago)
            slug = title.lower().replace(' ', '-').replace('/', '-')[:50]

            article, created = Article.objects.get_or_create(
                slug=slug,
                defaults={
                    'author': user,
                    'title': title,
                    'summary': f'This is a detailed tutorial about {title} covering core knowledge and practical experience.',
                    'body': body_template,
                    'category': category,
                    'views': random.randint(100, 5000),
                    'is_top': i < 3,
                    'create_date': create_date,
                }
            )
            if created:
                article.tags.set(article_tags)
                self.stdout.write(f'Created: {title}')

        # Create friend links
        friends_data = [
            ('Ruan Yifeng Blog', 'http://www.ruanyifeng.com', 'https://www.ruanyifeng.com/favicon.ico'),
            ('Liao Xuefeng', 'https://www.liaoxuefeng.com', 'https://www.liaoxuefeng.com/favicon.ico'),
            ('GitHub', 'https://github.com', 'https://github.githubassets.com/favicons/favicon.svg'),
            ('Stack Overflow', 'https://stackoverflow.com', 'https://cdn.sstatic.net/Sites/stackoverflow/Img/favicon.ico'),
        ]

        for name, link, logo in friends_data:
            friend, created = FriendLink.objects.get_or_create(
                name=name,
                defaults={
                    'description': f'{name} is an excellent tech website',
                    'link': link,
                    'logo': logo,
                    'is_show': True,
                }
            )
            if created:
                self.stdout.write(f'Created friend: {name}')

        self.stdout.write(self.style.SUCCESS(
            f'\nTotal: Category={Category.objects.count()}, Tag={Tag.objects.count()}, '
            f'Article={Article.objects.count()}, FriendLink={FriendLink.objects.count()}'
        ))
