from django.contrib import admin
from .models import Course, Car, Carousel, Category, Order


# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'grade', 'suitable_for_croud', 'category']
    list_filter = ['category']
    fields = ['name', 'grade', 'suitable_for_croud', 'category', 'image_url']


class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'course', 'count']
    list_filter = ['user', 'course']
    fields = ['user', 'course', 'count']


class CarouselAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_path']


class CategorylAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'course', 'count', 'sum', 'date', 'is_active']
    list_filter = ['user']

admin.site.register(Course, CourseAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Category, CategorylAdmin)
admin.site.register(Order, OrderAdmin)
