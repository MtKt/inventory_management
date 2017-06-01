from django.conf.urls import url
from . import views

app_name = 'i_m'
urlpatterns = [
                url(r'^$', views.IndexView.as_view(), name = 'index'),
                url(r'^bill/(?P<bill_id>\w+)$', views.BillView.as_view(), name = 'bill' ),
                url(r'^bills/$', views.Bills_all_View.as_view(), name = 'bills'),
                url(r'companies/$', views.CompaniesView.as_view(),name = 'companies'),
                url(r'^company/(?P<company_id>\w+)/$', views.CompanyView.as_view(), name ='company'),
              ]