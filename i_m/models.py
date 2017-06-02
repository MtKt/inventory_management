from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse

# Create your models here.

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField('姓名',max_length = 40)
    department = models.CharField('部门',max_length = 40)
    position = models.CharField('职位',max_length = 40)
    tel = models.CharField('联系方式',max_length = 40)
    create_time = models.DateTimeField('入职时间', auto_now_add=True)
    #staff_id = models.CharField('员工ID',max_length = 40,unique=True,default=0)

    '''def save(self, *args, **kwargs):
        self.staff_id = 'STF'+self.pk
        super().save(*args, **kwargs)'''

    def __str__(self):
        return self.name

class Company(models.Model):

    LEVEL = {
        0:u'A',
        1:u'B',
        2:u'C'
    }
    name = models.CharField('名称',max_length = 40)
    contact = models.CharField('负责人',max_length = 40)
    area = models.CharField('地区',max_length = 40)
    tel = models.CharField('联系方式',max_length = 40)
    create_time = models.DateTimeField('录入时间', auto_now_add=True)
    level = models.IntegerField('客户等级', default=0, choices=LEVEL.items())
    #company_id = models.CharField('公司ID',max_length = 40,blank = True)
    '''def save(self, *args, **kwargs):
        self.company_id = 'CSTMR'+self.create_time
        super().save(*args, **kwargs)'''

    def get_absolute_url(self):
        return reverse('i_m:company', kwargs={'company_id': self.id})

    def __str__(self):
        return self.name

'''@receiver(post_save, sender = Company)
def update_company_id(sender, **kwargs):
    Company.company_id = 'CSTMR'+str(Company.id)
    Company.save()'''

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
    product_name = models.CharField('货物名称', max_length = 40)
    quantity = models.IntegerField('需求数量')
    #bill_id = models.CharField('账单ID',max_length = 40,unique=True)

    '''def save(self, *args, **kwargs):
        self.company_id = 'BILL'+str(self.create_time)+str(self.pk)
        super().save(*args, **kwargs)'''

    def get_absolute_url(self):
        return reverse('i_m:bill', kwargs={'bill_id': self.id})

    def __str__(self):
        return self.company_name.name

class Dispatch(models.Model):
    STATUS = {
        0:u'已审阅',
        1:u'草稿'
    }
    sales_name = models.ForeignKey(Staff, verbose_name=u'销售人员', on_delete=models.CASCADE)
    company_name = models.ForeignKey(Company, verbose_name=u'公司', on_delete=models.CASCADE)
    bill = models.OneToOneField(Bill, verbose_name=u'订单', on_delete=models.CASCADE)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    dispatch_time = models.DateTimeField('发货时间', auto_now_add=False)
    dispatch_status = models.IntegerField('单证状态', default=0, choices=STATUS.items())
    product_name = models.CharField('货物名称', max_length = 40)
    quantity = models.IntegerField('交货数量')

    def get_absolute_url(self):
        return reverse('i_m:dispatch', kwargs={'dispatch_id': self.id})

    def __str__(self):
        return str(self.create_time)