from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils import timezone
from operator import attrgetter
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *

def menu_list(request):
    all_menus = Menu.objects.prefetch_related(
        'items'
    ).all().order_by('-expiration_date')
    menus = []
    for menu in all_menus:
        menu_items = menu,  menu.items.all()
        if not menu.expiration_date:
            menus.insert(0, menu_items)
        else:
            menus.append(menu_items)

    return render(request, 'menu/list_all_current_menus.html', {'menus': menus})

def menu_detail(request, pk):
    menu = Menu.objects.prefetch_related(
        'items'
    ).get(pk=pk)
    return render(request, 'menu/menu_detail.html', {'menu': menu})

def item_detail(request, pk):
    try: 
        item = Item.objects.select_related(
            'chef'
        ).prefetch_related(
            'ingredients'
        ).get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404
    return render(request, 'menu/detail_item.html', {'item': item})

def create_new_menu(request):
    if request.method == "POST":
        form = MenuForm(data=request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.created_date = timezone.now()
            menu.save()
            menu.items = request.POST.getlist('items')
            menu.save()
            return redirect('menu_detail', pk=menu.pk)
    else:
        form = MenuForm()
    return render(request, 'menu/menu_edit.html', {
            'form': form,
            'title': "Create menu"
        })

def edit_menu(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == "POST":
        form = MenuForm(instance=menu, data=request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.items = request.POST.getlist('items')            
            menu.save()
        return redirect('menu_detail', pk=menu.pk)

    else:
        form = MenuForm(instance=menu)
    return render(request, 'menu/menu_edit.html', {
            'form': form,
            'title': "Edit menu"
        })