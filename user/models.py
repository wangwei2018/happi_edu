from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone


# Create your models here.

class Carousel(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    # 轮播图片
    image_path = models.CharField(max_length=100, verbose_name='图片链接')

    class Meta:
        db_table = 'carousel'


class Category(models.Model):
    '''
    课程类别
    '''
    id = models.AutoField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=100, verbose_name='课程类别')

    class Meta:
        db_table = 'course_category'

    def __str__(self):
        return self.name


class Course(models.Model):
    '''
    课程表单
    '''
    id = models.AutoField(primary_key=True, verbose_name='id')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=100, verbose_name='课程名称')
    grade = models.FloatField(verbose_name='评分')
    suitable_for_croud = models.CharField(max_length=100, verbose_name='适用人群')
    image_url = models.CharField(max_length=200, verbose_name='图片链接地址')
    price = models.IntegerField(verbose_name='单价', default=1000)

    class Meta:
        db_table = 'course'

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='cars', verbose_name='用户')
    course = models.ForeignKey(to=Course, on_delete=models.PROTECT, related_name='car', verbose_name='课程')
    count = models.IntegerField(verbose_name='数量')

    class Meta:
        db_table = 'car'


class Order(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='orders', verbose_name='用户')
    course = models.ForeignKey(to=Course, on_delete=models.PROTECT, related_name='orders', verbose_name='课程')
    count = models.IntegerField(verbose_name='数量')
    sum = models.IntegerField(verbose_name='订单总价')
    date = models.DateTimeField(default=timezone.now, verbose_name='订单生成时间')
    is_active = models.BooleanField(default=True, verbose_name='订单状态')

    class Meta:
        db_table = 'my_order'
