from django.shortcuts import render
import random
from .models import Car, Details



def index(request):
    return render(request, 'main/index.html')


def russian_auto(request):
    return render(request, 'main/russian_car.html')


def details_list(request):
    details = Details.objects.all().order_by('-id')
    return render(request, 'main/details.html', {'details': details})


def car_list(request):
    cars = Car.objects.all().order_by('-id')  # Получаем все объекты модели Car
    return render(request, 'main/car.html', {'cars': cars})




def home(request):
    images = [
        'https://avatars.mds.yandex.net/i?id=697a199272ac3b5c36569f9f4b0995f5bc42caeb-5237646-images-thumbs&n=13',
        'https://avatars.mds.yandex.net/i?id=9e064e0acfdea3890e73993138c9ac539123b8b8-5520101-images-thumbs&n=13'
    ]
    random_image_url = random.choice(images)
    return render(request, 'index.html', {'images': random_image_url})

