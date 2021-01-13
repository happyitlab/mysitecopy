from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    # slug : url에 텍스트 주소가 있어도 인식되도록 함
    slug = models.SlugField(unique=False, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/blog/category/{}'.format(self.slug)

    class Meta:
        verbose_name_plural = "categories"


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    # 이미지 필드 추가
    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)

    created = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} :: {}'.format(self.title, self.author)

    def get_absolute_url(self):
        return '/blog/{}/'.format(self.pk)

    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)


class SearchList(models.Model):
    searchword = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True) #현재 시간으로 자동으로 설정

    def __str__(self):
        return self.searchword






