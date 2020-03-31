from django import forms
from pj_manage.models import Project
from django.forms import ModelForm


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['project_price_area', 'name']
        labels = {
            'project_price_area': '采购方式',
            'name': '项目名称',
        }