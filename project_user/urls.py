from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='user-login'),
    path('logout/', views.user_logout, name='user-logout'),
    path('dashboard/admin', views.admin_index, name='admin-index'),


    path('dashboard/admin/staff/add', views.add_staff, name='add-staff'),
    path('dashboard/admin/staff/all', views.all_staffs, name='all-staff'),
    path('dashboard/admin/staff/profile/edit/<int:pid>', views.edit_staff_profile, name='edit-staff-profile'),
    path('dashboard/admin/staff/profile/password/edit/<int:pid>', views.edit_staff_password, name='edit-staff-password'),
    path('dashboard/admin/staff/delete/<int:pid>', views.delete_staff, name='delete-staff'),
    path('dashboard/admin/additional/staff/profile/info/add/<int:pid>', views.staff_additional_profile_info, name='add-additional-info-staff'),

    path('dashboard/admin/client/add', views.client_add, name='add_client'),
    path('dashboard/admin/client/all', views.all_clients, name='all-client'),
    path('dashboard/admin/client/profile/edit/<int:pid>', views.edit_client_profile, name='edit-client-profile'),
    path('dashboard/admin/client/profile/password/edit/<int:pid>', views.edit_client_password, name='edit-client-password'),
    path('dashboard/admin/client/delete/<int:pid>', views.delete_client, name='delete-client'),
    path('dashboard/admin/additional/client/profile/info/add/<int:pid>', views.client_additional_profile_info, name='add-additional-info-client'),

    path('dashboard/satff', views.staff_index, name='staff-index'),
    path('dashboard/client', views.client_index, name='client-index'),

]
