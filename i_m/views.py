from collections import defaultdict
from os.path import join
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Bill,Staff,Company
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, TemplateView
import datetime

class IndexView(TemplateView):
    template_name = 'i_m/index.html'

'''

class Bills_all_View(ListView):#可以的话还是改成request()，先用这个续上
    model = Bill
    template_name = 'i_m/bills.html'
    context_object_name = 'bills_list'
    paginate_by = 8
    
    def get_queryset(self):
        bills_list = Bill.objects.filter(bill_status=0).order_by("-create_time")
        return bills_list


class TimeView(TemplateView):#可以的话还是改成request()，先用这个续上
    template_name = 'i_m/timeline.html'
    def get_context_data(self,**kwargs):
        model = Bill
        bills_list = Bill.objects.filter(bill_status=0).order_by("-create_time")
        year_all = defaultdict(list)
        for bill in bills_list:
            year = bill.pub_date.year
            year_all[year].append(bill)
        year_all=sorted(year_all.items(),reverse=True)
        context = super(TimeView,self).get_context_data(**kwargs)
        context['year_all'] = year_all
        context['bills_list'] = bills_list
        return context
'''

class BillView(DetailView):
    template_name = 'i_m/bill.html'
    model = Bill
    context_object_name = 'bill'
    pk_url_kwarg = 'bill_id' 

def bills(request):
    bills_list = Bill.objects.filter(bill_status=0).order_by("-create_time")
    context=dict()
    if 'year_from' and 'month_from' and 'day_from' and\
            'year_to' and 'month_to' and 'day_to' in request.GET:
        y = request.GET['year_from']
        m = request.GET['month_from']
        d = request.GET['day_from']
        date_from = datetime.datetime(int(y), int(m), int(d), 0, 0)
        y = request.GET['year_to']
        m = request.GET['month_to']
        d = request.GET['day_to']
        date_to = datetime.datetime(int(y), int(m), int(d), 0, 0)
        bills_list = Bill.objects.filter(create_time__range=(date_from, date_to)).order_by("-create_time")
    else:
        print ("error time range!")
    context['bills_list'] = bills_list
    return render(request,"i_m/bills.html",context)

def companies(request):
    bills_list = Company.objects.order_by("-create_time")
    context=dict()
    if 'year_from' and 'month_from' and 'day_from' and\
            'year_to' and 'month_to' and 'day_to' in request.GET:
        y = request.GET['year_from']
        m = request.GET['month_from']
        d = request.GET['day_from']
        date_from = datetime.datetime(int(y), int(m), int(d), 0, 0)
        y = request.GET['year_to']
        m = request.GET['month_to']
        d = request.GET['day_to']
        date_to = datetime.datetime(int(y), int(m), int(d), 0, 0)
        bills_list = Company.objects.filter(create_time__range=(date_from, date_to)).order_by("-create_time")
    else:
        print ("error time range!")
    context['companies_list'] = bills_list
    return render(request,"i_m/companies.html",context)

class CompanyView(DetailView):
    template_name = 'i_m/company.html'
    model = Company
    context_object_name = 'company'
    pk_url_kwarg = 'company_id' 
 