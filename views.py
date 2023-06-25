from django.shortcuts import render
from .models import MenuItem

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'base.html')

def menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})

def menu_item(request, item_id):
    menu_item = MenuItem.objects.get(pk=item_id)
    return render(request, 'menu_item.html', {'menu_item': menu_item})
