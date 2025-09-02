from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

app_name = 'accounts'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name="logout"),
    path('registration/', user_registration_view, name='registration'),
    path('role-selection/', UserRoleSelectionView.as_view(), name='role_selection'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('password-change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(
        template_name='accounts/password_reset_form.html',
        email_template_name='accounts/password_reset_email.html',
        success_url=reverse_lazy('accounts:password_reset_done')
        ), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
            name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        success_url=reverse_lazy('accounts:password_reset_complete')
    ), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
            name='password_reset_complete'),
    path('activate/<uuid:token>/', ActivateUserView.as_view(), name='activate'),
    path('verification-email/', VerificationEmailView.as_view(), name='verification_email'),
]
