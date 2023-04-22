from django.contrib.auth import views as auth
from django.urls import path

from accounts.views import RegisterView, ProfileDetailView

urlpatterns = [
    path('login/', auth.LoginView.as_view(), name='login'),
    path('logout/', auth.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail')
]
