from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250, verbose_name='заголовок поста')
    slug = models.SlugField(max_length=250, unique_for_date='publish', verbose_name='метка')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField(verbose_name='тело поста')
    publish = models.DateTimeField(default=timezone.now, verbose_name='время публикации поста')
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания поста')
    updated = models.DateTimeField(auto_now=True, verbose_name='дата и время последнего обновления поста')
    status = models.CharField(max_length=2, choices=Status.choices,
                              default=Status.DRAFT)
    objects = models.Manager()  # менеджер, применяемый по умолчанию
    published = PublishedManager()  # конкретно-прикладной менеджер

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Метод get_absolute_url(), возвращает канонический URL-адрес объекта"""
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
