from django.urls import path
from . import views


urlpatterns = [
    path('details/add/', views.add_project_details, name='add-add_project-details'),
    path('development/tools/add/<int:pid>', views.add_development_tools, name='add-development-tools'),
    path('role/management/<int:pid>', views.project_role, name='role-management'),
    path('designation/get/<name>', views.get_designation_id),
    path('team/delete/<int:pid>', views.delete_project_team, name='delete_project_team'),
    path('payment/type/<int:pid>', views.get_payment, name='add_project-get-payment'),
    path('payment/type/feature/<int:pid>', views.get_feature_payment),
    path('payment/type/monthly/<int:pid>', views.get_monthly_payment),
    path('payment/service/<int:pid>', views.get_service_charge),
    path('delete/<int:pid>', views.delete_project, name="project-delete"),
    path('details/overview/<int:pid>', views.project_details_overview, name='project-details-overview'),


    path('team/details/<int:pid>', views.project_team_details, name='project-team-details'),
    path('timeline/details/<int:pid>', views.project_timeline, name='project-timeline'),
    path('todo/lists/<int:pid>', views.project_todo_list, name='project-todo-list'),
    path('todo/lists/delete/<int:pid>', views.delete_todo_list, name='todo-list-delete'),
    path('feedback/<int:pid>', views.project_feedback, name='project-feedback'),
    path('payment/details/<int:pid>', views.project_payments, name='project-payment'),
    path('client/details/<int:pid>', views.project_client_details, name='project-client-details'),
]
