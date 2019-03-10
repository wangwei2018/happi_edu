from django.urls import re_path
from . import views

urlpatterns = [
    re_path('^$', views.index, name='index'),
    re_path('index/$', views.index, name='index'),
    re_path('login/$', views.login, name='login'),
    re_path('register/$', views.register, name='register'),
    re_path('logout/$', views.logout, name='logout'),
    re_path('get_show_info/$', views.get_show_info, name='get_show_info'),
    re_path('carousel/$', views.carousel, name='carousel'),
    re_path('get_more_info/$', views.get_more_info, name='get_more_info'),
    re_path('show_info/(\d+)$', views.show_info, name='show_info'),
    re_path('add_car/$', views.add_car, name='add_car'),
    re_path('my_car/$', views.my_car, name='my_car'),
    re_path('get_car_info/$', views.get_car_info, name='get_car_info'),
    re_path('delete/$', views.delete, name='delete'),
    re_path('add/$', views.add, name='add'),
    re_path('reduce/$', views.reduce, name='reduce'),
    re_path('search/$', views.search, name='search'),
    re_path('my_order/$', views.submit_order, name='submit_order'),
    re_path('pay/$', views.pay, name='pay'),
    re_path('get_order_info/$', views.get_order_info, name='get_order_info'),
    re_path('delete_order/$', views.delete_order, name='delete_order'),
]
