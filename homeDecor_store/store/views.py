from django.shortcuts import render

def home_page(request):
    context = {

    }
    return render(request, 'home.html', context)

def new_item(request):
    return render(request, 'add_item.html')
