from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Inventory

# Create your views here.


def search_inventory_entries(request):
    inventory_object = Inventory.objects.all()
    inventory_search = request.GET.get('Journal_Entry')
    if inventory_search != '' and inventory_search is not None:
        inventory_object = inventory_object.filter(Item_Name__icontains=inventory_search) | inventory_object.filter(
            Item_Price__icontains=inventory_search) | inventory_object.filter(
            Item_Description__icontains=inventory_search) | inventory_object.filter(
            Item_Ingredients__icontains=inventory_search) | inventory_object.filter(
            Item_Amount_in_Inventory__icontains=inventory_search)
    else:
        "<p> Search not Available <p>"
    paginator = Paginator(inventory_object, 5)
    page = request.GET.get('page')
    inventory_object = paginator.get_page(page)
    return render(request, 'JoeyStoreApp/inventory_search.html', {'inventory_object': inventory_object})



