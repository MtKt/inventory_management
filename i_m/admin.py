from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from i_m.models import Staff,Company,Bill

class StaffInline(admin.StackedInline):
    model = Staff
    can_delete = False
    verbose_name_plural = 'staff'

class UserAdmin(BaseUserAdmin):
    inlines = (StaffInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Bill)
admin.site.register(Company)

