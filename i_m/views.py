from collections import defaultdict
from os.path import join
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Bill,Staff,Company,Dispatch
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, TemplateView
import datetime

class IndexView(TemplateView):
    template_name = 'i_m/index.html'

def search(objs_list,Obj,request,context):
    if 'year_from' and 'month_from' and 'day_from' and 'year_to' and 'month_to' and 'day_to' in request.GET:
        try:
            y = request.GET['year_from']
            m = request.GET['month_from']
            d = request.GET['day_from']
            date_from = datetime.datetime(int(y), int(m), int(d), 0, 0)
            y = request.GET['year_to']
            m = request.GET['month_to']
            d = request.GET['day_to']
            date_to = datetime.datetime(int(y), int(m), int(d), 0, 0)
            objs_list = Obj.objects.filter(create_time__range=(date_from, date_to)).order_by("-create_time")
            context['objs_list'] = objs_list
            if not objs_list:
                context['ERR'] = '╮(￣▽￣"")╭  并没有查到什么'
                context['objs_list'] = ''
        except:
            context['ERR'] = '╮(￣▽￣"")╭  并没有查到什么'
            context['objs_list'] = ''
    return context


def bills(request):
    bills_list = Bill.objects.filter(bill_status=0).order_by("-create_time")
    context=dict()
    context['bills_list'] = bills_list
    #search(bills_list,Bill,request,context)
    if 'year_from' and 'month_from' and 'day_from' and\
            'year_to' and 'month_to' and 'day_to' in request.GET:
        try:
            y = request.GET['year_from']
            m = request.GET['month_from']
            d = request.GET['day_from']
            date_from = datetime.datetime(int(y), int(m), int(d), 0, 0)
            y = request.GET['year_to']
            m = request.GET['month_to']
            d = request.GET['day_to']
            date_to = datetime.datetime(int(y), int(m), int(d), 0, 0)
            bills_list = Bill.objects.filter(create_time__range=(date_from, date_to)).order_by("-create_time")
            if not bills_list:
                context['ERR'] = '╮(￣▽￣"")╭  并没有查到什么'
        except:
            context['ERR'] = '╮(￣▽￣"")╭  并没有查到什么'
            bills_list = ''
        
        if bills_serial in request:
            pass

    context['bills_list'] = bills_list
    return render(request,"i_m/bills.html",context)

class BillView(DetailView):
    template_name = 'i_m/bill.html'
    model = Bill
    context_object_name = 'bill'
    pk_url_kwarg = 'bill_id' 

def companies(request):
    companies_list = Company.objects.order_by("-create_time")
    context=dict()
    #search(companies_list,Company,request,context)
    if 'year_from' and 'month_from' and 'day_from' and\
            'year_to' and 'month_to' and 'day_to' in request.GET:
        try:
            y = request.GET['year_from']
            m = request.GET['month_from']
            d = request.GET['day_from']
            date_from = datetime.datetime(int(y), int(m), int(d), 0, 0)
            y = request.GET['year_to']
            m = request.GET['month_to']
            d = request.GET['day_to']
            date_to = datetime.datetime(int(y), int(m), int(d), 0, 0)
            companies_list = Company.objects.filter(create_time__range=(date_from, date_to)).order_by("-create_time")
            if not companies_list:
                context['ERR'] = '╮(￣▽￣"")╭  并没有查到什么'
        except:
            context['ERR'] = '╮(￣▽￣"")╭  并没有查到什么'
            companies_list = ''
    context['companies_list'] = companies_list
    return render(request,"i_m/companies.html",context)

class CompanyView(DetailView):
    template_name = 'i_m/company.html'
    model = Company
    context_object_name = 'company'
    pk_url_kwarg = 'company_id'

def dispatchs(request):
    dispatchs_list = Dispatch.objects.order_by("-create_time")
    context=dict()
    context['ERR']=''

    #search(dispatchs_list,Dispatch,request,context)

    if 'year_from' and 'month_from' and 'day_from' and\
            'year_to' and 'month_to' and 'day_to' in request.GET:
        try:
            y = request.GET['year_from']
            m = request.GET['month_from']
            d = request.GET['day_from']
            date_from = datetime.datetime(int(y), int(m), int(d), 0, 0)
            y = request.GET['year_to']
            m = request.GET['month_to']
            d = request.GET['day_to']
            date_to = datetime.datetime(int(y), int(m), int(d), 0, 0)
            dispatchs_list = Dispatch.objects.filter(create_time__range=(date_from, date_to)).order_by("-create_time")
            if not dispatchs_list:
                context['ERR'] = '╮(￣▽￣"")╭  并没有查到什么'
        except:
            context['ERR'] = '╮(￣▽￣"")╭  并没有查到什么'
            dispatchs_list = ''

    context['dispatchs_list'] = dispatchs_list
    return render(request,"i_m/dispatchs.html",context)

class DispatchView(DetailView):
    model = Dispatch
    template_name = 'i_m/dispatch.html'
    context_object_name = 'dispatch'
    pk_url_kwarg = 'dispatch_id' 