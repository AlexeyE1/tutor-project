from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

# Create your views here.

class HomeView(TemplateView):
    template_name = 'main/home.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['session'] = self.request.session
        return context



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
