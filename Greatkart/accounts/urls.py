from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('forgot/', views.forgot, name='forgot'),
    path('reset/<uidb64>/<token>/', views.reset, name='reset'),
    path('resetpass/', views.resetpass, name='resetpass'),
]
