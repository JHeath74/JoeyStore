from django import forms
from .models import Inventory


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['Item_Name', 'Item_Price', 'Item_Description', 'Item_Ingredients', 'Item_Amount_in_Inventory',
                  'Item_Images', 'university', 'previous_work', 'skills']
