from PackageApp.models import Package
from travelplanner.DynamicFieldsModel import DynamicFieldsModelSerializer


class PackageSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

class  PackageDropdownSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Package
        fields = ['name']