from django.conf.urls import url
from . import views

app_name = 'i_m'
urlpatterns = [
                url(r'^$', views.IndexView.as_view(), name = 'index'),
                url(r'^bill/(?P<category_id>\w+)$', views.AboutView.as_view(), name = 'bill' ),
                url(r'^bills/$', views.TimeLine.as_view(), name = 'bills'),
                url(r'companies/$', views.CategoryView.as_view(),name = 'company'),
                url(r'^company/(?P<company_id>\w+)/$', views.cyuuni_detail, name ='companies'),
              ]