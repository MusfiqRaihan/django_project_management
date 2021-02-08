from django import forms
from .models import ProjectDetail



class CreateProjectDetailForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(
            attrs={'type': 'date'}))

    completion_date = forms.DateField(widget=forms.DateInput(
            attrs={'type': 'date'}))


    class Meta:
        model = ProjectDetail
        fields = [
            'title',
            'company_name',
            'company_email',
            'company_phone',
            'company_address',
            'start_date',
            'completion_date',
            'project_summary',
            'project_goal',
            'project_impact',
            'project_requirement',
            'development_methodology',
        ]
