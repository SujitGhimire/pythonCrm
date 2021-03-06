from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import Lead
from .forms import LeadForm

def lead_list(request):
    leads=Lead.objects.all()
    context={
        "leads":leads
    }
    return render(request,"leads/index.html",context)

def lead_detail(request,pk):
    lead=Lead.objects.get(id=pk)
    context={
        "lead":lead
    }
    return render(request,"leads/lead_details.html",context)

def lead_create(request):
    print(request.POST)
    context={
        "forms":LeadForm()
    }
    return render(request,"leads/lead_create.html",context)