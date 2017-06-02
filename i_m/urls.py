from django.conf.urls import url
from . import views

app_name = 'i_m'
urlpatterns = [
                url(r'^$', views.IndexView.as_view(), name = 'index'),
                url(r'^bill/(?P<bill_id>\w+)$', views.BillView.as_view(), name = 'bill' ),
                url(r'^bills/$', views.bills, name = 'bills'),
                url(r'companies/$', views.companies, name = 'companies'),
                url(r'^company/(?P<company_id>\w+)/$', views.CompanyView.as_view(), name ='company'),
                url(r'dispatchs/$', views.dispatchs, name = 'dispatchs'),
                url(r'^dispatch/(?P<dispatch_id>\w+)/$', views.DispatchView.as_view(), name ='dispatch'),
              ]