from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def home_view(request):
    """Главная страница сайта"""
    context = {
        'title': 'Главная - Наставник',
        'page_title': 'Найдите лучшего наставника',
        'page_description': 'Платформа для поиска квалифицированных наставников и репетиторов'
    }
    return render(request, 'main/home.html', context)

# def about_view(request):
#     """Страница о нас"""
#     context = {
#         'title': 'О нас - Наставник',
#         'page_title': 'О платформе Наставник',
#         'page_description': 'Узнайте больше о нашей платформе для поиска наставников'
#     }
#     return render(request, 'main/about.html', context)

# def contact_view(request):
#     """Страница контактов"""
#     context = {
#         'title': 'Контакты - Наставник',
#         'page_title': 'Свяжитесь с нами',
#         'page_description': 'Контактная информация и форма обратной связи'
#     }
#     return render(request, 'main/contact.html', context)
