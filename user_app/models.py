from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

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
        ordering = ['dp_id']


class Section(models.Model):
    section_id = models.SmallIntegerField(verbose_name='科室编号')
    name = models.CharField(max_length=64, null=True, verbose_name='科室名称')
    department = models.ForeignKey('Department', verbose_name='所属部门', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '科室总表'
        verbose_name_plural = '科室总表'


class MyUserManage(BaseUserManager):

    def create_user(self, user_id, username, password=None):
        user = self.model(
            user_id=user_id,
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, username, password=None):
        user = self.create_user(
            user_id=user_id,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    '''不含权限以及分组管理'''
    user_id = models.CharField(max_length=16, verbose_name='员工编号', unique=True)
    username = models.CharField(verbose_name='姓名', max_length=64)
    section = models.ForeignKey('Section', verbose_name='所属科室', null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey('Department', verbose_name='所属部门', null=True, on_delete=models.SET_NULL)
    plat = models.ForeignKey('Plat', verbose_name='所属平台', null=True, on_delete=models.SET_NULL)
    phone = models.CharField(max_length=32, verbose_name='电话')
    mobile_phone = models.CharField(max_length=32, verbose_name='手机')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManage()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return '%s %s %s' % (self.user_id, self.username, self.department)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name = '员工总表'
        verbose_name_plural = '员工总表'

