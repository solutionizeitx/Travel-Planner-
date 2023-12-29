

from HotelApp.models import Hotel, Hoteltype
from LocationApp.serializers import LocationSerializer
from travelplanner.DynamicFieldsModel import DynamicFieldsModelSerializer


class HoteltypeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Hoteltype
        fields = '__all__'


class HotelSerializer(DynamicFieldsModelSerializer):

    location = LocationSerializer()
    type = HoteltypeSerializer()

    class Meta:
        model = Hotel
        fields = '__all__'


class HotelDropdownSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'is_active']


class HoteltypeDropdownSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Hoteltype
        fields = ['id', 'name', 'is_active']
