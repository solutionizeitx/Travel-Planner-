from django.shortcuts import render
from HotelApp.serializers import *
from travelplanner.common_functions import MESSAGE, STATUS, ResponseFunction, ValidateRequest, printLineNo
from travelplanner.global_imports import *
from HotelApp.models import *
# Create your views here.

class HotelAPI(ListAPIView):

    serializer_class = HotelSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        pagination = self.request.GET.get('pagination', '1')
        if pagination == '0':
            print("Pagination None")
            self.pagination_class = None

        id = self.request.GET.get('id', '')
        name = self.request.GET.get('name', '')
        is_dropdown = self.request.GET.get('is_dropdown', False)

        if is_dropdown=='1':
            print("Drop down get request")
            self.serializer_class = HotelDropdownSerializer

        qs = Hotel.objects.all()

        if id: qs = qs.filter(id=id) # check and explain

        if name: qs = qs.filter(name__icontains=name) # check and explain

        return qs

    def post(self, request):
        print("REQUST DATA : ==> ",request.data)
        required = ["name"]
        validation_errors = ValidateRequest(required, self.request.data)

        if len(validation_errors) > 0:
            return ResponseFunction(0, validation_errors[0]['error'],{})
        else:
            print("Receved required Fields")


        try:
            id = self.request.POST.get('id', '')
            if id:
                print("Hotel Updating")
                qs = Hotel.objects.filter(id=id)
                if not qs.count():
                    return ResponseFunction(0, "Hotel Not Found",{})
                variant_obj = qs.first()
                serializer = HotelSerializer(variant_obj, data=request.data, partial=True)
                msg = "Data updated"
            else:
                print("Adding new Hotel")
                serializer = HotelSerializer(data=request.data, partial=True)
                msg = "Data saved"
            serializer.is_valid(raise_exception=True)

            obj = serializer.save()
            return ResponseFunction(1, msg,HotelSerializer(obj).data)

        except Exception as e:
            print("Excepction ", printLineNo(), " : ", e)
            return ResponseFunction(0,f"Excepction occured {str(e)}",{})

    def delete(self, request):
        try:
            id = self.request.GET.get('id', "[]")
            if id == "all":

                Hotel.objects.all().delete()
                return ResponseFunction(1, "Deleted all data",{})

            else:
                id = json.loads(id)
                Hotel.objects.filter(id__in=id).delete()
                return ResponseFunction(1, "Deleted data having id " + str(id),{})

        except Exception as e:
            print("Excepction ", printLineNo(), " : ", e)
            return ResponseFunction(0,f"Excepction occured {str(e)}",{})