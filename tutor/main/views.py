from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

# Create your views here.

class HomeView(TemplateView):
    template_name = 'main/home.html'

    
    def post(request, *args, **kwargs):
        role = request.POST.get('role')
        if role in ['student', 'teacher']:
            request.session['role'] = role
            return redirect(reverse_lazy('accounts:registration'))


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
