from rest_framework import serializers
from workersApp.models import MenuItems


class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItems
        fields = ['id','item_name','item_description','item_price','item_inventory']





