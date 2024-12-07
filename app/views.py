import os

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, reverse

from datetime import datetime


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def time_view(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    current_time = datetime.now().time()
    msg = f'Текущее время: {current_time.strftime('%H:%M')}'
    return HttpResponse(msg)

def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории
    files_in_current_dir = []
    dir_user = os.getcwd()
    files = os.listdir(dir_user)
    for item in files:
        if '.' in item[1:]:
            files_in_current_dir.append(item)
    return HttpResponse(f'Список файлов: {files_in_current_dir}')
