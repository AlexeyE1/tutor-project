from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import StudentRegistrationForm, TeacherRegistrationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect

# # Create your views here.

def user_registration_view(request):
    role = request.session.get('role')
    if role not in ['student', 'teacher']:
        return redirect('main:home')

    form_class = StudentRegistrationForm if role == 'student' else TeacherRegistrationForm

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('user:login'))
    else:
        form = form_class()

    template_name = 'accounts/student_registration.html' if role == 'student' else 'accounts/teacher_registration.html'
    return render(request, template_name, {'form': form})
        
    

    



# def register_view(request):
#     return render(request, 'accounts/register.html')

# def logout_view(request):
#     return render(request, 'accounts/logout.html')

# def profile_view(request):
#     return render(request, 'accounts/profile.html')
