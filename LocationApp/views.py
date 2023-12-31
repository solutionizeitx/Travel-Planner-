from django.shortcuts import render
from HotelApp.serializers import *
from LocationApp.serializers import LocationSerializer, LocationDropdownSerializer
from travelplanner.common_functions import MESSAGE, STATUS, ResponseFunction, ValidateRequest, printLineNo
from travelplanner.global_imports import *
from LocationApp.models import *


class LocationAPI(ListAPIView):

    serializer_class = LocationSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # pagination = self.request.GET.get('pagination', '1')
        # if pagination == '0':
        #     print("Pagination None")
        #     self.pagination_class = None

        id = self.request.GET.get('id', '')
        name = self.request.GET.get('name', '')
        is_active = self.request.GET.get('is_active', '')
        is_dropdown = self.request.GET.get('is_dropdown', False)

        if is_dropdown=='1':
            print("Drop down get request")
            self.serializer_class = LocationDropdownSerializer

        qs = Location.objects.all()

        if id: qs = qs.filter(id=id)

        if name: qs = qs.filter(name__icontains=name)
        print("type of is_active=",type(is_active))
        if is_active: qs = qs.filter(is_active=is_active)


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
                print("Location Updating")
                qs = Location.objects.filter(id=id)
                if not qs.count():
                    return ResponseFunction(0, "Location Not Found",{})
                variant_obj = qs.first()
                serializer = LocationSerializer(variant_obj, data=request.data, partial=True)
                msg = "Data updated"
            else:
                print("Adding new Location")
                serializer = LocationSerializer(data=request.data, partial=True)
                msg = "Data saved"
            serializer.is_valid(raise_exception=True)

            obj = serializer.save()
            return ResponseFunction(1, msg,LocationSerializer(obj).data)

        except Exception as e:
            print("Excepction ", printLineNo(), " : ", e)
            return ResponseFunction(0,f"Excepction occured {str(e)}",{})

    def delete(self, request):
        try:
            id = self.request.GET.get('id', "[]")
            if id == "all":

                Location.objects.all().delete()
                return ResponseFunction(1, "Deleted all data",{})

            else:
                id = json.loads(id)
                Location.objects.filter(id__in=id).delete()
                return ResponseFunction(1, "Deleted data having id " + str(id),{})

        except Exception as e:
            print("Excepction ", printLineNo(), " : ", e)
            return ResponseFunction(0,f"Excepction occured {str(e)}",{})