

from django.shortcuts import render
from UserApp.serializers import *
from UserApp.serializers import UserModelSerializer, UserModelDropdownSerializer
from travelplanner.common_functions import MESSAGE, STATUS, ResponseFunction, ValidateRequest, printLineNo
from travelplanner.global_imports import *
from UserApp.models import *


class UserAPI(ListAPIView):

    serializer_class = UserModelSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # pagination = self.request.GET.get('pagination', '1')
        # if pagination == '0':
        #     print("Pagination None")
        #     self.pagination_class = None

        id = self.request.GET.get('id', '')
        user_name = self.request.GET.get('user_name', '')
        is_dropdown = self.request.GET.get('is_dropdown', False)

        if is_dropdown == '1':
            print("Drop down get request")
            self.serializer_class = UserModelDropdownSerializer

        from UserApp.models import UserModel
        qs = UserModel.objects.all()

        if id:
            qs = qs.filter(id=id)  # check and explain

        if user_name:
            qs = qs.filter(user_name=user_name)  # check and explain

        return qs

    def post(self, request):
        print("REQUST DATA : ==> ", request.data)
        required = ["username", "mobile_number"]
        validation_errors = ValidateRequest(required, self.request.data)

        if len(validation_errors) > 0:
            return ResponseFunction(0, validation_errors[0]['error'], {})
        else:
            print("Receved required Fields")

        try:
            user_obj = None
            id = request.data.get('id', None)

            if id:
                _qs = UserModel.objects.filter(id=id)

                if _qs.exists():
                    data = _qs.first()
                else:
                    return ResponseFunction(0, "User not found", {})

                _serializer = UserModelSerializer(
                    data, data=request.data, many=False, partial=True)
                msg = "User updated successfully"
            else:
                _serializer = UserModelSerializer(
                    data=request.data, many=False, partial=True)
                msg = "User created successfully"

            password = self.request.data.get('password', '')
            print("password is ", password)

            if _serializer.is_valid(raise_exception=True):
                if password:
                    msg = "User details and password updated"
                    user_obj = _serializer.save(
                        password=make_password(password))
                else:
                    msg = "User details updated"
                    user_obj = _serializer.save()
                data = _serializer.data

            return ResponseFunction(1, msg, data)
        except Exception as e:
            msg = f"Excepction occured UserDetailsAPI Post {e} error at {printLineNo()}"
            print(msg)
            if user_obj:
                user_obj.delete()
                print("User deleted")

            return ResponseFunction(0, msg, str(request.data))

    def delete(self, request):
        try:
            id = self.request.GET.get('id', "[]")
            if id == "all":

                UserModel.objects.all().delete()
                return ResponseFunction(1, "Deleted all data", {})

            else:
                id = json.loads(id)
                UserModel.objects.filter(id__in=id).delete()
                return ResponseFunction(1, "Deleted data having id " + str(id), {})

        except Exception as e:
            print("Excepction ", printLineNo(), " : ", e)
            return ResponseFunction(0, f"Excepction occured {str(e)}", {})


class UserLoginAPI(ObtainAuthToken):
    def post(self, request, *args, **kwargs):

        # from django.contrib.auth.hashers import check_password
        from django.contrib.auth import authenticate
        print("post worked")
        data = {}
        msg = ""

        try:
            username = self.request.POST.get('username', '')
            password = self.request.POST.get('password', '')

            if username and password:
                password = password
                # user = authenticate(username=username, password=password)

                print("password is ", password)
                serializer = self.serializer_class(data=request.data,
                                                   context={'request': request})
                test = serializer.is_valid(raise_exception=True)
                user = serializer.validated_data['user']
                # user = UserDetails.objects.filter(
                #     username=username, password=password)

                print("user is ", user)

                if user:
                    if user.is_active:
                        # login(request, user)
                        data = {
                            'username': user.username,
                            'id': user.id,
                            'email': user.email,
                            'first_name': user.first_name,
                            'last_name': user.last_name,
                            'is_superuser': user.is_superuser,
                            'is_staff': user.is_staff,
                            'is_active': user.is_active,
                            'mobile_number': user.mobile_number,
                        }
                        return ResponseFunction(1, "User logged in", data)
                    else:
                        return ResponseFunction(0, "User is not active", {})
                else:
                    return ResponseFunction(0, "Invalid credentials", {})
            else:
                return ResponseFunction(0, "Username and password required", {})
        except Exception as e:
            msg = f"Excepction occured UserLoginAPI Post {e} error at {printLineNo()}"
            print(msg)
            return ResponseFunction(0, msg,  str(request.data))
