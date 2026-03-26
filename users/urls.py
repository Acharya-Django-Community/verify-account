from django.urls import path
from .views import register , verify_otp
from django.contrib.auth.views import LoginView , LogoutView , PasswordResetView , PasswordResetDoneView , PasswordResetConfirmView , PasswordResetCompleteView
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('password-reset/',PasswordResetView.as_view(template_name='reset.html'),name='password_reset'),
    path('reset-done/',PasswordResetDoneView.as_view(template_name='reset.done.html'),name='password_reset_done'),
    path('confirm-reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='confirm.html'),name='password_reset_confirm'),
    path('complete-reset-password/',PasswordResetCompleteView.as_view(template_name='reset_complete.html'),name='password_reset_complete')

]