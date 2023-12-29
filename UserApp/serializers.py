from travelplanner.DynamicFieldsModel import DynamicFieldsModelSerializer
from UserApp.models import UserModel
class UserModelSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

class  UserModelDropdownSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = UserModel
        fields = ['name']