from django.urls import path
from django.contrib.auth import views as auth_views
from .views import MyLoginView, MyLogoutView, SignUpView 

urlpatterns = [
    # Login URL
    path('login/', MyLoginView.as_view(), name='login'),

    # Logout URL
    path('logout/', MyLogoutView.as_view(), name='logout'),

    path('signup/', SignUpView.as_view(), name='signup'),

    # Password reset URLs (ensure these are correctly configured in your project)
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
