# users/urls.py

from django.urls import path
from .views import MyProfile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # URL for the user profile page
    path('profile/', MyProfile.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
