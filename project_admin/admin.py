from django.contrib import admin
from .models import Development_Tool, development_methodology, Development_Member, Payment_type


class Development_ToolModel(admin.ModelAdmin):
    list_display = ["__str__", "development_method", "development_name", "created_on"]
    list_per_page = 10
    list_filter = ('development_method',)

    class Meta:
        model = Development_Tool


admin.site.register(Development_Tool, Development_ToolModel)


class development_methodologyModel(admin.ModelAdmin):
    list_display = ["__str__", "name", "created_on"]
    list_per_page = 10

    class Meta:
        model = development_methodology


admin.site.register(development_methodology, development_methodologyModel)


class Development_MemberModel(admin.ModelAdmin):
    list_display = ["__str__", "name", "position", "created_on"]
    list_per_page = 10
    list_filter = ('position',)

    class Meta:
        model = Development_Member


admin.site.register(Development_Member, Development_MemberModel)


class Payment_typeModel(admin.ModelAdmin):
    list_display = ["__str__", "name", "created_on"]
    list_per_page = 10

    class Meta:
        model = Payment_type


admin.site.register(Payment_type, Payment_typeModel)
