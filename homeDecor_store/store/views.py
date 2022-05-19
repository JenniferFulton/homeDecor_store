import re
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def home_page(request):
    #home page displays inventory with option to add new item to inventory
    all_items = Item.objects.all()
    context = {
        'inventory' : all_items
    }
    return render(request, 'home.html', context)

def new_item(request):
    #brings user to a page where there is a form to add new item and 
    #option to add a new warehouse
    all_warehouses = Warehouse.objects.all()
    context = {
        'locations' : all_warehouses
    }
    return render(request, 'add_item.html', context)

def new_warehouse(request):
    #brings user to a page with a form to add a new warehouse location and
    #show current warehouse locations
    all_warehouses = Warehouse.objects.all()
    context = {
        'locations' : all_warehouses
    }
    return render(request, 'add_warehouse.html', context)

def warehouse_success(request):
    #adds a new warehouse and goes back to warehouse page
    if request.method == 'POST':
        errors = Warehouse.objects.newWarehouse_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/new_warehouse')
        else:
            Warehouse.objects.create(
            name = request.POST['name'],
            address = request.POST['address'],
            city = request.POST['city'],
            state = request.POST['state'],
            zip_code = request.POST['zip_code'],
                )
            return redirect('/new_warehouse')

def item_success(request):
    #adds a new item to inventory
    if request.method == 'POST':
        errors = Item.objects.newItem_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/new_item')
        else:
            Item.objects.create(
            name = request.POST['name'],
            description = request.POST['description'],
            height = request.POST['height'],
            width = request.POST['width'],
            color = request.POST['color'],
            quantity = request.POST['quantity'],
            image = request.POST['image']
                )

            location = Warehouse.objects.get(id = request.POST['location'])
            last_item = Item.objects.last()
            location.warehouse.add(last_item)

            return redirect('/')

def edit_item(request,id):
    #brings user to a page with a form to edit a specific item
    current_item = Item.objects.get(id=id)
    all_warehouses = Warehouse.objects.all()
    context = {
        'locations' : all_warehouses,
        'item' : current_item,
    }
    return render(request, 'edit_item.html', context)

def edit_success(request,id):
    #updates item information
    if request.method == 'POST':
        # errors = Item.objects.newItem_validator(request.POST)
        # if len(errors) > 0:
        #     for key, value in errors.items():
        #         messages.error(request, value)
        #     return redirect('/view_item/' + str(id))
        # else:
        to_edit = Item.objects.get(id=id)
        to_edit.name = request.POST['new_name']
        to_edit.description = request.POST['new_description']
        to_edit.height = request.POST['new_height']
        to_edit.width = request.POST['new_width']
        to_edit.color = request.POST['new_color']
        to_edit.quantity = request.POST['new_quantity']
        
        location = Warehouse.objects.get(id = request.POST['new_location'])
        location.warehouse.add(to_edit)

        to_edit.save()

        return redirect('/')

def delete_item(request,id):
    #delete an item in the inventory and send user back to home page
    to_delete = Item.objects.get(id=id)
    to_delete.delete()
    return redirect('/')

def view_item(request,id):
    #view a specific item
    current_item = Item.objects.get(id=id)
    context = {
        'item': current_item
    }

    return render(request, 'view_item.html', context)


    