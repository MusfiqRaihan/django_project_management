from django.contrib import admin
from project_user.models import Profile



class ProfileModel(admin.ModelAdmin):
    list_display = ["id", "user", "phone_number", "address"]
    list_per_page = 10
    list_filter = ['user']

    class Meta:
        model = Profile


admin.site.register(Profile, ProfileModel)
