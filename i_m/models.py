from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField('姓名',max_length = 40)
    department = models.CharField('部门',max_length = 40)
    position = models.CharField('职位',max_length = 40)
    tel = models.CharField('联系方式',max_length = 40)
    create_time = models.DateTimeField('入职时间', auto_now_add=True)
    staff_id = models.CharField('员工ID',max_length = 40,unique=True)

    def __str__(self):
        return self.staff_id

class Company(models.Model):
    name = models.CharField('名称',max_length = 40)
    contact = models.CharField('负责人',max_length = 40)
    area = models.CharField('地区',max_length = 40)
    tel = models.CharField('联系方式',max_length = 40)
    create_time = models.DateTimeField('录入时间', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('i_m:company', kwargs={'bill_id': self.id})

    def __str__(self):
        return self.name

class Bill(models.Model):

    STATUS = {
        0:u'已审阅',
        1:u'草稿'
    }

    sales_name = models.ForeignKey(Staff, verbose_name=u'销售人员', on_delete=models.CASCADE)
    company_name = models.ForeignKey(Company, verbose_name=u'公司', on_delete=models.CASCADE)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    deliver_time = models.DateTimeField('交货时间', auto_now_add=False)
    bill_status = models.IntegerField('单证状态', default=0, choices=STATUS.items())
    product_name = models.CharField('名称', max_length = 40)
    quantity = models.IntegerField('数量')
    bill_id = models.CharField('账单ID',max_length = 40,unique=True)

    def get_absolute_url(self):
        return reverse('i_m:bill', kwargs={'bill_id': self.id})

    def __str__(self):
        return self.bill_id