

from HotelApp.models import Hotel
from travelplanner.DynamicFieldsModel import DynamicFieldsModelSerializer


class  HotelSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class  HotelDropdownSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id','name','is_active']
