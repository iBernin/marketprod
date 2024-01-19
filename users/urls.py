from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
import users.views as mpauth

app_name = 'mpauth'

urlpatterns = [
    path('register/', mpauth.MpUserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/confirm', mpauth.logout_confirm, name='logout-confirm'),
]