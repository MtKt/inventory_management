from django.db import models

# Create your models here.
ARTICLE_STATUS = {
        0:u'已审阅',
        1:u'草稿'
    }

class Bill(object):
    company_name = models.CharField('客户名称',max_length = 40)
    department = medels.CharField('部门',max_length = 40)
    position = models.CharField('职位',max_length = 40)
    tel = models.CharField('联系方式',max_length = 40)
    create_time = models.DateTimeField('入职时间', auto_now_add=True)

        

class Staff(object):
    name = models.CharField('姓名',max_length = 40)
    department = medels.CharField('部门',max_length = 40)
    position = models.CharField('职位',max_length = 40)
    tel = models.CharField('联系方式',max_length = 40)
    create_time = models.DateTimeField('入职时间', auto_now_add=True)

class Compamy(object):
    name = models.CharField('名称',max_length = 40)
    contact = medels.CharField('负责人',max_length = 40)
    area = models.CharField('地区',max_length = 40)
    tel = models.CharField('联系方式',max_length = 40)
    create_time = models.DateTimeField('录入时间', auto_now_add=True)