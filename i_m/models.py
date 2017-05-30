from django.db import models

# Create your models here.


class Staff(object):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField('姓名',max_length = 40)
    department = medels.CharField('部门',max_length = 40)
    position = models.CharField('职位',max_length = 40)
    tel = models.CharField('联系方式',max_length = 40)
    create_time = models.DateTimeField('入职时间', auto_now_add=True)

    def __str__(self):
        return '员工' + self.pk

class Compamy(object):
    name = models.CharField('名称',max_length = 40)
    contact = medels.CharField('负责人',max_length = 40)
    area = models.CharField('地区',max_length = 40)
    tel = models.CharField('联系方式',max_length = 40)
    create_time = models.DateTimeField('录入时间', auto_now_add=True)

    def get_absolute_url(self):
        return reverse('i_m:company', kwargs={'bill_id': self.id})

    def __str__(self):
        return '公司' + self.pk


class Bill(object):

    STATUS = {
        0:u'已审阅',
        1:u'草稿'
    }

    sales_name = medels.ForeignKey(Staff,verbose_name=u'销售人员')
    company_name = medels.ForeignKey(Staff,verbose_name=u'公司')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    deliver_time = models.DateTimeField('交货时间', auto_now_add=False)
    bill_status = models.IntegerField('单证状态', default=0, choices=STATUS.items())
    product_name = models.CharField('名称', max_length = 40)
    quantity = models.IntegerField('数量')

    def get_absolute_url(self):
        return reverse('i_m:bill', kwargs={'bill_id': self.id})

    def __str__(self):
        return '订单号' + self.pk

