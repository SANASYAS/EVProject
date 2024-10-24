from django.urls import path
from .views import register,success_view,login_view,fleet_manager_home_view,driver_home_view

urlpatterns = [
    path('register/', register, name='register'),
    path('success/', success_view, name='success_url'),  # Success URL
    path('login/', login_view, name='login'),
    # Define other URLs for fleet manager and driver pages
    path('fleet_manager_home/', fleet_manager_home_view, name='fleet_manager_home'),
    path('driver_home/', driver_home_view, name='driver_home'),
]

