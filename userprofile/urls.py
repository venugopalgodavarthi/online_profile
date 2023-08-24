from django.urls import path
from userprofile import views
app_name = 'user'
urlpatterns = [
    path('register/', views.register_profile, name='register'),
    path('display/<pk>/', views.display_profile, name='display'),
    path('details/', views.details_profile, name='details'),
    path('update/<pk>/', views.update_profile, name='update'),
    path('delete/<pk>/', views.delete_profile, name='delete'),
]
