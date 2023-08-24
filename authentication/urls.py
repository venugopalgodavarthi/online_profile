from django.urls import path, include
from authentication import views
app_name = "authe"
urlpatterns = [
    path('userregister/', views.register_user, name="userregister"),
    path('userlogin/', views.login_user, name="userlogin"),
    path('userlogout/', views.logout_user, name="userlogout"),
]
