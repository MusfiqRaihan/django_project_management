from django.urls import path
from . import views

urlpatterns = [

    path('developers/add', views.add_developers, name='add-developers'),
    path('developers/delete/<int:pid>', views.delete_developers, name='delete-developers'),

    path('developemnt/tools/add', views.add_development_tools, name='add-development-tools'),
    path('developemnt/tools/delete/<int:pid>', views.delete_development_tools, name='delete-development-tools'),

    path('development/method/add', views.add_development_method, name='add-development-method'),
    path('development/method/delete/<int:pid>', views.delete_development_method, name='delete-development-method'),

    path('payment/types/add', views.add_payment_types, name='add-payment-types'),
    path('payment/types/delete/<int:pid>', views.delete_payment_types, name='delete-payment-types'),

]
