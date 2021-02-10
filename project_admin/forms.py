from django import forms
from project_admin.models import Development_Member, Development_Tool, development_methodology, Payment_type


class AddDevelopersForm(forms.ModelForm):
    class Meta:
        model = Development_Member
        fields = [
            'name',
            'position',
        ]


class AddDevelopmentToolsForm(forms.ModelForm):
    class Meta:
        model = Development_Tool
        fields = [
            'development_method',
            'development_name',
        ]



class AddDevelopmentMethodForm(forms.ModelForm):
    class Meta:
        model = development_methodology
        fields = [
            'name',
        ]


class AddPaymentTypeForm(forms.ModelForm):
    class Meta:
        model = Payment_type
        fields = [
            'name',
        ]
