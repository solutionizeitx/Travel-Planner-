from PackageApp.models import Package, PackageType
from travelplanner.DynamicFieldsModel import DynamicFieldsModelSerializer
from rest_framework import serializers
from LocationApp.serializers import LocationSerializer


class PackageTypeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = PackageType
        fields = '__all__'


class PackageSerializer(DynamicFieldsModelSerializer):

    location = LocationSerializer()
    type = PackageTypeSerializer()

    class Meta:
        model = Package
        fields = '__all__'


class PackageDropdownSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Package
        fields = ['name']


class PackageTypeDropdownSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = PackageType
        fields = ['name']
