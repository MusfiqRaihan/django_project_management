from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_login, name='user-login'),
    path('logout/', views.user_logout, name='user-logout'),
    path('dashboard/admin', views.admin_index, name='admin-index'),
    path('dashboard/satff', views.staff_index, name='staff-index'),
    path('dashboard/client', views.client_index, name='client-index'),
    path('add/staff', views.add_staff, name='add-staff'),
    path('dashboard/staff/all', views.all_staff_lists, name='all-staff-list'),
    path('dashboard/client/all', views.all_client_lists, name='all-client-list'),
    path('add/client', views.add_client, name='add-client'),

]
