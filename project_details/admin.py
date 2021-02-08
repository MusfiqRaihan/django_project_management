from django.contrib import admin
from .models import ProjectDetail, \
    ToDoList, ProjectDevelopmentTool, \
    ProjectTeamMember, ProjectFeaturePayment, \
    ProjectServiceCharge, ClientProfile,\
    Timeline_User, ProjectPaymentDone, ProjectMonthlyPayment

admin.site.site_header = 'PROJECT MANAGEMENT ADMIN PANEL'


class ProjectDetailModel(admin.ModelAdmin):
    list_display = ["__str__", "id", "profile_name", "company_name", "development_methodology", "completion_date"]
    list_per_page = 10
    list_filter = ('company_name', 'development_methodology', )

    class Meta:
        model = ProjectDetail


admin.site.register(ProjectDetail, ProjectDetailModel)


class ProjectDevelopmentToolModel(admin.ModelAdmin):
    list_display = ["__str__", "profile_name", "fronted", "backend",
                    "database", "server_side", "repository", "created_on"]
    list_per_page = 10
    list_filter = ('project_name', 'profile_name', )

    class Meta:
        model = ProjectDevelopmentTool


admin.site.register(ProjectDevelopmentTool, ProjectDevelopmentToolModel)


class ProjectTeamMemberModel(admin.ModelAdmin):
    list_display = ["__str__", "project_name", "profile_name", "designation", "member_name", "created_on"]
    list_per_page = 10
    list_filter = ('project_name', 'profile_name')

    class Meta:
        model = ProjectTeamMember


admin.site.register(ProjectTeamMember, ProjectTeamMemberModel)




class ProjectFeaturePaymentModel(admin.ModelAdmin):
    list_display = ["__str__", "profile_name", "feature", "created_on"]
    list_per_page = 10
    list_filter = ('project_name', 'profile_name')

    class Meta:
        model = ProjectFeaturePayment


admin.site.register(ProjectFeaturePayment, ProjectFeaturePaymentModel)


class ProjectMonthlyPaymentModel(admin.ModelAdmin):
    list_display = ["__str__", "profile_name", "monthly", "created_on"]
    list_per_page = 10
    list_filter = ('project_name', 'profile_name')

    class Meta:
        model = ProjectMonthlyPayment


admin.site.register(ProjectMonthlyPayment, ProjectMonthlyPaymentModel)





class ProjectServiceChargeModel(admin.ModelAdmin):
    list_display = ["__str__", "profile_name", "service", "total", "created_on"]
    list_per_page = 10
    list_filter = ('project_name', 'profile_name')

    class Meta:
        model = ProjectServiceCharge


admin.site.register(ProjectServiceCharge, ProjectServiceChargeModel)


class ClientProfileModel(admin.ModelAdmin):
    list_display = ["__str__", "project_name", "profile_name", "email", "client_phone", "created_on"]
    list_per_page = 10
    list_filter = ('project_name', 'profile_name')

    class Meta:
        model = ClientProfile


admin.site.register(ClientProfile, ClientProfileModel)



# class ToDoListModel(admin.ModelAdmin):
#     list_display = ["__str__", "project_name", "todo", "created_on"]
#     list_per_page = 10
#     list_filter = ('project_name', 'staff')
#
#     class Meta:
#         model = ToDoList
#
#
# admin.site.register(ToDoList, ToDoListModel)



class Timeline_UserModel(admin.ModelAdmin):
    list_display = ["__str__", "id", "profile_name", "start_date", "completion_date",
                    "update_completion_date", "created_on"]
    list_per_page = 10

    class Meta:
        model = Timeline_User


admin.site.register(Timeline_User, Timeline_UserModel)


class ProjectPaymentDoneModel(admin.ModelAdmin):
    list_display = ["__str__", "id", "profile_name", "budget", "previous_payment", "due", "created_on"]
    list_per_page = 10

    class Meta:
        model = ProjectPaymentDone


admin.site.register(ProjectPaymentDone, ProjectPaymentDoneModel)
