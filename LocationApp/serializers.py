from LocationApp.models import Location
from travelplanner.DynamicFieldsModel import DynamicFieldsModelSerializer


class  LocationSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class  LocationDropdownSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Location
        fields = ['name']