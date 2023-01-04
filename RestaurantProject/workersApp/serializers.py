from rest_framework import serializers
from .models import MenuItems

class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItems
        fields = ['id','item_name','item_description','item_price','item_inventory']
        extra_kwargs = {
            'item_price':{'min_value' : 2},
            'item_inventory' : {'min_value' : 0}
        }




