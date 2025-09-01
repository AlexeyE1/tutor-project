from django.shortcuts import render
from django.views.generic import ListView
from accounts.models import TeacherProfile, SubjectTag, LearningTypeTag



class HomeView(ListView):
    model = TeacherProfile
    template_name = 'catalog/home.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        learning_type_ids = self.request.GET.getlist('learning_type')
        subject_tag_ids = self.request.GET.getlist('subject_tag')
        rating_min = self.request.GET.get('rating_min')
        price_min = self.request.GET.get('price_min')
        price_max = self.request.GET.get('price_max')
        experience_min = self.request.GET.get('experience_min')

        # Filter queryset based on the selected filters
        if experience_min:
            queryset = queryset.filter(experience_years__gte=experience_min)
        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)
        if rating_min:
            queryset = queryset.filter(avg_rating__gte=rating_min)
        if learning_type_ids:
            queryset = queryset.filter(learning_types__id__in=learning_type_ids)
        if subject_tag_ids:
            queryset = queryset.filter(subjects__id__in=subject_tag_ids)

        return queryset.prefetch_related('learning_types', 'subjects')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['learning_types'] = LearningTypeTag.objects.all()
        context['subject_tags'] = SubjectTag.objects.all()
        context['selected_learning_types'] = self.request.GET.getlist('learning_type')
        context['selected_subject_tags'] = self.request.GET.getlist('subject_tag')
        return context