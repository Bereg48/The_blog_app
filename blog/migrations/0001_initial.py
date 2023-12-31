# Generated by Django 4.2.5 on 2023-10-01 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='заголовок поста')),
                ('slug', models.SlugField(max_length=250, verbose_name='метка')),
                ('body', models.TextField(verbose_name='тело поста')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='время публикации поста')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания поста')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='дата и время последнего обновления поста')),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publish'],
                'indexes': [models.Index(fields=['-publish'], name='blog_post_publish_bb7600_idx')],
            },
        ),
    ]
