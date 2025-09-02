from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, View
from .forms import *
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.http import Http404
import uuid


class UserRoleSelectionView(TemplateView):
    template_name = 'accounts/role_selection.html'

    def post(self, request, *args, **kwargs):
        role = request.POST.get('role')
        print(role)
        if role not in ['student', 'teacher']:
            messages.error(request, 'Выберите корректную роль.')
            return redirect('accounts:role_selection')
        request.session['role'] = role
        return redirect('accounts:registration')
    

def user_registration_view(request):
    role = request.session.get('role')
    if role not in ['student', 'teacher']:
        return redirect('main:home')

    form_class = StudentRegistrationForm if role == 'student' else TeacherRegistrationForm

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            send_verification_email(request, user)
            messages.success(request, 'Регистрация успешна! Проверьте ваш email для подтверждения аккаунта.')
            return redirect('accounts:email_verification')
    else:
        form = form_class()

    template_name = 'accounts/student_registration.html' if role == 'student' else 'accounts/teacher_registration.html'
    return render(request, template_name, {'form': form})


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main:home')


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserProfileForm(instance=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form = UserProfileForm(request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect(reverse_lazy('user:profile'))
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = 'accounts/password_change_form.html'

    def form_valid(self, form):
        messages.success(self.request, 'Password changed successfully.')
        return super().form_valid(form)


# Отправка email для подтверждения
def send_verification_email(request, user):
    current_site = get_current_site(request)
    verification_url = reverse('accounts:activate', kwargs={'token': str(user.verification_token)})
    full_url = f"{request.scheme}://{current_site.domain}{verification_url}"

    message = render_to_string('accounts/verification_email.html', {
        'user': user,
        'verification_url': full_url,
        'site_name': current_site.name
    })

    send_mail(
        subject='Подтвердите ваш email - TutorHub',
        message=message,
        from_email='noreply@tutorhub.com',  # Замените на ваш email
        recipient_list=[user.email],
        fail_silently=False,
        html_message=message
    )


class ActivateUserView(View):
    def get(self, request, token):
        try:
            user = get_object_or_404(get_user_model(), verification_token=token)
            if not user.email_confirmed:
                user.email_confirmed = True
                user.save()
                return render(request, 'accounts/email_verification.html', {
                    'verification_success': True
                })
            else:
                return render(request, 'accounts/email_verification.html', {
                    'verification_error': True,
                    'error_message': 'Ваш email уже подтвержден.'
                })
        except Exception as e:
            return render(request, 'accounts/email_verification.html', {
                'verification_error': True,
                'error_message': 'Недействительная ссылка для подтверждения.'
            })

class VerificationEmailView(View):
    def get(self, request):
        return render(request, 'accounts/verification_email.html')