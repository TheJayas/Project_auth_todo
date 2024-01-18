from django.urls import path,include
from rest_framework import routers    
from . import views
router = routers.DefaultRouter()                      # add this
router.register(r'tasks', views.TodoView, 'task')     # add this

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('changepassword/', views.UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', views.SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),    
    path('reset-password/<uid>/<token>/', views.UserPasswordResetView.as_view(), name='reset-password'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    # path('tasks/', views.TodoView.as_view(), name='profile'),
    path('', include(router.urls))

]