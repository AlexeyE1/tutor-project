from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from .models import CustomUser, MentorProfile


class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['email', 'password']



class BaseRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    email = forms.EmailField(label='Email')
    age = forms.IntegerField(label='Возраст', required=False)
    phone = forms.IntegerField(label='Телефон', required=False)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'age', 'phone', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Такой Email уже существует')
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and get_user_model().objects.filter(phone=phone).exists():
            raise forms.ValidationError('Аккаунт с таким номером телефона уже существует')
        return phone


class StudentRegistrationForm(BaseRegistrationForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'student'
        if commit:
            user.save()
        return user


class TeacherRegistrationForm(BaseRegistrationForm):
    subjects = forms.ModelMultipleChoiceField(
        queryset=MentorProfile._meta.get_field('subjects').related_model.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    learning_types = forms.ModelMultipleChoiceField(
        queryset=MentorProfile._meta.get_field('learning_types').related_model.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    bio = forms.CharField(widget=forms.Textarea, required=False)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'teacher'
        if commit:
            user.save()
            mentor_profile = MentorProfile.objects.create(
                user=user,
                bio=self.cleaned_data.get('bio', '')
            )
            mentor_profile.subjects.set(self.cleaned_data['subjects'])
            mentor_profile.learning_types.set(self.cleaned_data['learning_types'])
        return user


class UserProfileForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['avatar', 'first_name', 'last_name', 'email']

    avatar = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(label="Подтверждение пароля",
                                    widget=forms.PasswordInput(attrs={'class': 'form-input'}))