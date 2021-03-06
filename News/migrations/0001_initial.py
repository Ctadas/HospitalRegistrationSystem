# Generated by Django 2.1.7 on 2019-03-11 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=100, verbose_name='轮播图片主题')),
                ('image', models.ImageField(upload_to='CarouselMap/%Y/%m/%d/', verbose_name='轮播图片')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='新闻标题')),
                ('content', models.TextField(max_length=5000, verbose_name='新闻内容')),
                ('image', models.ImageField(upload_to='news/%Y/%m/%d/', verbose_name='新闻图片')),
                ('source', models.CharField(max_length=50, verbose_name='新闻来源')),
                ('release_time', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '新闻管理',
                'verbose_name_plural': '新闻管理',
            },
        ),
    ]
