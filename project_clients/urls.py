from django.urls import path
from . import views


urlpatterns = [
    path('logout/', views.client_logout, name='client-logout'),
    path('profile/', views.client_profile, name='client-profile'),
    path('profile/edit/', views.edit_client_profile, name='client-profile-edit'),
    path('profile/password/edit/', views.edit_client_password, name='client-password-edit'),
]
