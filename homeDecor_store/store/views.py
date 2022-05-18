from django.shortcuts import render
from .models import *

def home_page(request):
    all_items = Item.objects.all()
    context = {
        'inventory' : all_items
    }
    return render(request, 'home.html', context)

def new_item(request):
    return render(request, 'add_item.html')

def new_warehouse(request):
    return render(request, 'add_warehouse.html')
