from collections import defaultdict
from os.path import join
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Bill,Staff,Company
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Q

class IndexView(TemplateView):
    template_name = 'i_m/index.html'

class Bills_all_View(ListView):#可以的话还是改成request()，先用这个续上
    model = Bill
    template_name = 'i_m/bills.html'
    context_object_name = 'bills_list'
    paginate_by = 8
    
    def get_queryset(self):
        bills_list = Bill.objects.filter(status=0).order_by("-create_time")
        return bills_list

class BillView(DetailView):
    template_name = 'i_m/bill.html'
    model = Company
    context_object_name = 'bill'
    pk_url_kwarg = 'bill_id' 

class TimeView(TemplateView):#可以的话还是改成request()，先用这个续上
    template_name = 'i_m/timeline.html'
    def get_context_data(self,**kwargs):
        model = Bill
        bills_list = Bill.objects.filter(article_status=0).order_by("-create_time")
        year_all = defaultdict(list)
        for bill in bills_list:
            year = bill.pub_date.year
            year_all[year].append(bill)
        year_all=sorted(year_all.items(),reverse=True)
        context = super(TimeView,self).get_context_data(**kwargs)
        context['year_all'] = year_all
        context['bills_list'] = bills_list
        return context

#def bill(request):

class CompaniesView(ListView):
    model = Company
    template_name = 'i_m/companies.html'
    context_object_name = 'bills_list'
    paginate_by = 8
    
    def get_queryset(self):
        companies_list = Company.objects.filter(status=0).order_by("-create_time")
        return companies_list

class CompanyView(DetailView):
    template_name = 'i_m/company.html'
    model = Company
    context_object_name = 'company'
    pk_url_kwarg = 'company_id' 