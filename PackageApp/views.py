from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from HotelApp.serializers import *
from PackageApp.serializers import PackageSerializer,PackageDropdownSerializer
from travelplanner.common_functions import MESSAGE, STATUS, ResponseFunction, ValidateRequest, printLineNo
from travelplanner.global_imports import *
from PackageApp.models import *


class PackageAPI(ListAPIView):

    serializer_class = PackageSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # pagination = self.request.GET.get('pagination', '1')
        # if pagination == '0':
        #     print("Pagination None")
        #     self.pagination_class = None

        id = self.request.GET.get('id', '')
        name = self.request.GET.get('name', '')
        is_dropdown = self.request.GET.get('is_dropdown', False)

        if is_dropdown=='1':
            print("Drop down get request")
            self.serializer_class = PackageDropdownSerializer

        from PackageApp.models import Package
        qs = Package.objects.all()

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
                print("Package Updating")
                qs = Package.objects.filter(id=id)
                if not qs.count():
                    return ResponseFunction(0, "Package Not Found",{})
                variant_obj = qs.first()
                serializer = PackageSerializer(variant_obj, data=request.data, partial=True)
                msg = "Data updated"
            else:
                print("Adding new Package")
                serializer = PackageSerializer(data=request.data, partial=True)
                msg = "Data saved"
            serializer.is_valid(raise_exception=True)

            obj = serializer.save()
            return ResponseFunction(1, msg,PackageSerializer(obj).data)

        except Exception as e:
            print("Excepction ", printLineNo(), " : ", e)
            return ResponseFunction(0,f"Excepction occured {str(e)}",{})

    def delete(self, request):
        try:
            id = self.request.GET.get('id', "[]")
            if id == "all":

                Package.objects.all().delete()
                return ResponseFunction(1, "Deleted all data",{})

            else:
                id = json.loads(id)
                Package.objects.filter(id__in=id).delete()
                return ResponseFunction(1, "Deleted data having id " + str(id),{})

        except Exception as e:
            print("Excepction ", printLineNo(), " : ", e)
            return ResponseFunction(0,f"Excepction occured {str(e)}",{})