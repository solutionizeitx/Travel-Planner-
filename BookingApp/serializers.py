from BookingApp.models import Booking
from travelplanner.DynamicFieldsModel import DynamicFieldsModelSerializer
class  BookingSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class  BookingDropdownSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','packageName','hotel_name','typeName','booking_date_to','booking_date_from']