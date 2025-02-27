from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('token/refresh/', views.RefreshTokenView.as_view(), name='token_refresh'),
    path('token/verify/', views.VerifyTokenView.as_view(), name='token_verify'),

    path('profile/', views.ProfileView.as_view(), name='profile'),
]
