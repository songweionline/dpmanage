from django.db import models
from django.contrib.auth.models import User
from user_app.models import Plat, Department, Section, MyUser
import os
# Create your models here.


class Project(models.Model):  #共有属性

    project_price_area_choice = (
        ('odds', '1万以内零星采购'),
        ('inquiry', '1-10万询价采购'),
        ('internal', '10-30万内部招标'),
        ('public', '30万以上公开招标'),
    )

    project_type_choice = (
        ('consumables', '耗材'),
        ('service', '维修'),
        ('maintain', '维保'),
        ('protocol', '政府协议供货'),
        ('blu_rayDisc', '蓝光盘'),
        ('tape', '数据流磁带'),
        ('operations', '技术运营'),
    )

    project_price_area = models.CharField(choices=project_price_area_choice, max_length=64, verbose_name="采购方式")
    project_type = models.CharField(choices=project_type_choice, max_length=64, verbose_name='采购类型')
    name = models.CharField(max_length=128, verbose_name="项目名称")
    manufacturer = models.CharField(max_length=128, verbose_name="供应商名称")
    department = models.ForeignKey('user_app.Department', verbose_name="所属部门", on_delete=models.DO_NOTHING)
    budget = models.FloatField(verbose_name='项目预算')
    price = models.FloatField(verbose_name='项目总价')
    pj_user = models.ForeignKey('user_app.MyUser', verbose_name="使用人", on_delete=models.DO_NOTHING,
                                related_name='pj_user')
    charge_user = models.ForeignKey('user_app.MyUser', verbose_name="责任人", on_delete=models.DO_NOTHING,
                                    related_name='change_user')
    pj_operator = models.ForeignKey('user_app.MyUser', verbose_name='经办人', on_delete=models.DO_NOTHING,
                                    related_name='pj_operator')

    def __str__(self):
        return '<项目名称:%s>--<项目预算:%s>--<项目金额:%s>--<所属部门:%s>' % (self.name, self.budget, self.price,
                                                               self.department)

    class Meta:
        verbose_name = '项目总表'
        verbose_name_plural = '项目总表'






