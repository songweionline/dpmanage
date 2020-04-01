from django import forms
from pj_manage.models import Project
from django.forms import ModelForm


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        labels = {
            'project_price_area': '采购方式',
            'price_type': '项目类别',
            'name': '项目名称',
            'manufacturer': '供应商名称',
            'budget': '项目预算',
            'price': '项目总价',
            'pj_plat': '所属平台',
            'charge_user': '项目负责人',
            'department': '责任部门',
            'pj_operator': '经办人',
            'pj_user': '使用人',
        }