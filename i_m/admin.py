from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from i_m.models import Staff,Company,Bill,Dispatch
from django import forms

class StaffInline(admin.StackedInline):
    model = Staff
    can_delete = False
    verbose_name_plural = 'staff'

class UserAdmin(BaseUserAdmin):
    inlines = (StaffInline,)

class CompanyAdminForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ('company_id',)
class CompanyAdmin(admin.ModelAdmin):
    form = CompanyAdminForm

class BillAdminForm(forms.ModelForm):
    class Meta:
        model = Bill
        exclude = ('bill_id',)
class BillAdmin(admin.ModelAdmin):
	form = BillAdminForm

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Bill,BillAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Dispatch)
