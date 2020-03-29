from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Plat(models.Model):
    pt_id = models.SmallIntegerField(null=True, verbose_name="平台编号")
    name = models.CharField(max_length=64, null=True, verbose_name="平台名称")

    def __str__(self):
        return '%s %s' % (self.pt_id, self.name)

    class Meta:
        verbose_name = '平台总表'
        verbose_name_plural = '平台总表'
        ordering = ['pt_id']


class Department(models.Model):
    dp_id = models.SmallIntegerField(null=True, verbose_name="部门编号")
    name = models.CharField(max_length=64, null=True, verbose_name="部门名称")
    plat = models.ForeignKey('Plat', verbose_name='所属平台', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '%s %s' % (self.dp_id, self.name)

    class Meta:
        verbose_name = '部门总表'
        verbose_name_plural = '部门总表'


class Section(models.Model):
    section_id = models.SmallIntegerField(verbose_name='科室编号')
    name = models.CharField(max_length=64, null=True, verbose_name='科室名称')
    department = models.ForeignKey('Department', verbose_name='所属部门', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '科室总表'
        verbose_name_plural = '科室总表'


class EpProfile(models.Model):
    user = models.OneToOneField(User, verbose_name='员工总表', on_delete=models.CASCADE)
    department = models.ForeignKey('Department', verbose_name='所属部门', null=True, on_delete=models.SET_NULL)
    section = models.ForeignKey('Section', verbose_name='所属科室', null=True, on_delete=models.SET_NULL)
    uid = models.SmallIntegerField(unique=True, null=True, verbose_name='员工编号')
    phone = models.CharField(max_length=64, verbose_name='电话号码')

    def __str__(self):
        return '%s %s %s' % (self.user_id, self.user, self.department)

    class Meta:
        verbose_name = '员工总表'
        verbose_name_plural = '员工总表'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        EpProfile.objects.create(user = instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

