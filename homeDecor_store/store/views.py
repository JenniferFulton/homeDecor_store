from django.shortcuts import render, redirect
from .models import *

def home_page(request):
    all_items = Item.objects.all()
    context = {
        'inventory' : all_items
    }
    return render(request, 'home.html', context)

def new_item(request):
    all_warehouses = Warehouse.objects.all()
    context = {
        'locations' : all_warehouses
    }
    return render(request, 'add_item.html', context)

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

#edit a location

def item_success(request):
    if request.method == 'POST':
        Item.objects.create(
        name = request.POST['name'],
        description = request.POST['description'],
        height = request.POST['height'],
        width = request.POST['width'],
        color = request.POST['color'],
        quantity = request.POST['quantity'],
            )

        location = Warehouse.objects.get(id = request.POST['location'])
        last_item = Item.objects.last()
        location.warehouse.add(last_item)

        return redirect('/new_item')

def edit_item(request,id):
    current_item = Item.objects.get(id=id)
    all_warehouses = Warehouse.objects.all()
    context = {
        'locations' : all_warehouses,
        'item' : current_item,
    }
    return render(request, 'edit_item.html', context)

# def edit_success(request):


    