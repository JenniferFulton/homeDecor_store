from django.shortcuts import render, redirect
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
    all_warehouses = Warehouse.objects.all()
    context = {
        'locations' : all_warehouses
    }
    return render(request, 'add_warehouse.html', context)

def warehouse_success(request):
    if request.method == 'POST':
        Warehouse.objects.create(
        name = request.POST['name'],
        address = request.POST['address'],
        city = request.POST['city'],
        state = request.POST['state'],
        zip_code = request.POST['zip_code'],
            )
    return redirect('/new_warehouse')

