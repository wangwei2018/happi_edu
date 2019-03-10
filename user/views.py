from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import models
import json


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    if request.is_ajax():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponse('success')
        else:
            return HttpResponse('failed')
    else:
        status = request.GET.get('status')
        next = request.GET.get('next')
        return render(request, 'login.html', {'status': status, 'next': next})


def register(request):
    if request.is_ajax():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return HttpResponse('failed')
        else:
            new_user = User()
            new_user.username = username
            new_user.set_password(password)
            new_user.save()
            return HttpResponse('success')
    else:
        return render(request, 'register.html')


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index')


def get_show_info(request):
    if request.is_ajax():
        category_name = request.POST.get('category')
        category = models.Category.objects.get(name=category_name)
        courses = category.courses.all()
        info_list = []
        i = 0
        for course in courses:
            info = {}
            info['id'] = course.id
            info['src'] = course.image_url
            info['grade'] = course.grade
            info['name'] = course.name
            info_list.append(info)
            i += 1
            if i == 5:
                break
        return HttpResponse(json.dumps(info_list))


def carousel(request):
    if request.is_ajax():
        carousels = models.Carousel.objects.all().order_by('id')
        i = 0
        info_list = []
        for carousel in carousels:
            info_list.append(carousel.image_path)
            i += 1
            if i == 4:
                break
        return HttpResponse(json.dumps(info_list))


def get_more_info(request):
    if request.is_ajax():
        time = int(request.POST.get('time'))
        info_lists = []
        if time == 2:
            category_names = ['android', 'ai']

        else:
            category_names = ['ios', 'blockchain']

        for category_name in category_names:
            category = models.Category.objects.get(name=category_name)
            courses = category.courses.all()
            info_list = []
            i = 0
            for course in courses:
                info = {}
                info['id'] = course.id
                info['src'] = course.image_url
                info['grade'] = course.grade
                info['name'] = course.name
                info['category'] = category_name
                info_list.append(info)
                i += 1
                if i == 5:
                    break
            info_lists.append(info_list)
        return HttpResponse(json.dumps(info_lists))


def show_info(request, id):
    course = models.Course.objects.all().get(id=id)
    return render(request, 'course_info.html', {'course': course})


@login_required
def add_car(request):
    if request.is_ajax():
        id = request.POST.get('course_id')
        count = request.POST.get('count')
        course = models.Course.objects.get(id=id)
        try:
            my_car = models.Car.objects.get(course=course, user=request.user)
            my_car.count += int(count)
            my_car.save()

        except:
            new_car = models.Car()
            new_car.user = request.user
            new_car.course = course
            new_car.count = count
            new_car.save()

        return HttpResponse('success')


@login_required
def my_car(request):
    return render(request, 'car.html')


@login_required
def get_car_info(request):
    if request.is_ajax():
        cars = models.Car.objects.filter(user=request.user)
        info_list = []
        for item in cars:
            info = {}
            info['id'] = item.id
            info['name'] = item.course.name
            info['suit'] = item.course.suitable_for_croud
            info['count'] = item.count
            info['price'] = item.course.price
            info_list.append(info)
        return HttpResponse(json.dumps(info_list))


@login_required
def delete(request):
    if request.is_ajax():
        id = request.POST.get('id')
        car = models.Car.objects.get(id=id)
        car.delete()
        return HttpResponse('success')


@login_required
def add(request):
    if request.is_ajax():
        id = request.POST.get('id')
        car = models.Car.objects.get(id=id)
        car.count += 1
        car.save()
        return HttpResponse('success')


@login_required
def reduce(request):
    if request.is_ajax():
        id = request.POST.get('id')
        car = models.Car.objects.get(id=id)
        car.count -= 1
        car.save()
        return HttpResponse('success')


def search(request):
    if not request.is_ajax():
        key = request.GET.get('keyword')
        return render(request, 'searchResult.html', {'keyword': key})
    else:
        key = request.POST.get('key')
        items = models.Course.objects.filter(name__icontains=key)
        info_list = []
        for item in items:
            info = {}
            info['id'] = item.id
            info['name'] = item.name
            info['img'] = item.image_url
            info['grade'] = item.grade
            info['suit'] = item.suitable_for_croud
            info_list.append(info)

        return HttpResponse(json.dumps(info_list))


@login_required
def submit_order(request):
    if request.is_ajax():
        id_list = request.POST.get('ids')
        id_list = eval(id_list)
        # 从购物车中提交订单
        for id in id_list:
            car = models.Car.objects.get(id=id)
            new_order = models.Order()
            new_order.count = car.count
            new_order.user = request.user
            new_order.course = car.course
            new_order.sum = car.count * car.course.price
            new_order.save()
            car.delete()
        return HttpResponse('success')
    else:
        return render(request, 'my_order.html')


@login_required
def pay(request):
    return render(request, 'pay.html')


@login_required
def get_order_info(request):
    if request.is_ajax():
        orders = models.Order.objects.filter(user=request.user, is_active=True)
        info_list = []
        for item in orders:
            info = {}
            info['id'] = item.id
            info['name'] = item.course.name
            info['count'] = item.count
            info['sum'] = item.sum

            info['time'] = str(item.date).split('.')[0]
            info_list.append(info)
        return HttpResponse(json.dumps(info_list))


@login_required
def delete_order(request):
    if request.is_ajax():
        id_list = request.POST.get('ids')
        id_list = eval(id_list)
        for id in id_list:
            my_order = models.Order.objects.get(id=id)
            my_order.is_active = False
            my_order.save()
        return HttpResponse('success')
