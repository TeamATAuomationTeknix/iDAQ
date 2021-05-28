from .models import mst_dev_conn,units_table,mst_dev_addr,shift_table,mst_data,user_level,user_mng
from .serializers import mst_dev_conn_serializer,units_table_serializer,mst_dev_addr_serializer,shift_table_serializer,mst_data_serializer,user_level_serializer,user_mng_serializer,RegisterSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, permissions
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class mst_dev_conn_API(APIView):
    def get(self, request,pk=None,format = None):
        id = pk  # instead of pk you can give another field as in case it can be shift, unit etc
        if id is not None: # if in url you specify any int after / then it will consider this if code. take a look at url.py file for this
            devconn = mst_dev_conn.objects.get(id=id) # give model name here
            serializer = mst_dev_conn_serializer(devconn) # give serializer name here
            return Response(serializer.data)
        devconn = mst_dev_conn.objects.all() # if in url int is not specified then by default it will give you all data
        serializer = mst_dev_conn_serializer(devconn, many = True)
        return Response(serializer.data)

    def post(self, request,format = None):
        serializer = mst_dev_conn_serializer(data=request.data)
        if serializer.is_valid(): # if all fields are as per the specified formate then only it will save otherwise not & it is same for all
            serializer.save()
            return Response({'Device Added Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request,pk=None,format = None):
        id = pk
        devconn = mst_dev_conn.objects.get(pk=id)
        serializer = mst_dev_conn_serializer(devconn, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Device Updated Successfully'})
        return Response(serializer.errors)

    def delete(self, request,pk,format = None):
        id = pk
        devconn = mst_dev_conn.objects.get(pk=id)
        devconn.delete()
        return Response({'Device Deleted Successfully'})

class unit_table_API(APIView):
    def get(self, request,pk=None,format = None):
        id = pk
        if id is not None:
            unit = units_table.objects.get(id=id)
            serializer = units_table_serializer(unit)
            return Response(serializer.data)
        unit = units_table.objects.all()
        serializer = units_table_serializer(unit, many = True)
        return Response(serializer.data)

    def post(self, request,format = None):
        serializer = units_table_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Unit Added Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request,pk=None,format = None):
        id = pk
        unit = units_table.objects.get(pk=id)
        serializer = units_table_serializer(unit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Unit Updated Successfully'})
        return Response(serializer.errors)

    def delete(self, request,pk,format = None):
        id = pk
        unit = units_table.objects.get(pk=id)
        unit.delete()
        return Response({'Unit Deleted Successfully'})

class mst_dev_addr_API(APIView):
    # def get(self, request,pk=None,format = None):  # if want data wrt pk then uncomment it and also change the url
    def get(self, request,mst_dev_conn_id=None,format = None):
        # id = pk
        id = mst_dev_conn_id
        if id is not None:
            # devaddr = mst_dev_addr.objects.filter(id=mst_dev_conn_id)
            # serializer = mst_dev_addr_serializer(devaddr)
            # return Response(serializer.data)
            devaddr = mst_dev_addr.objects.all().filter(mst_dev_conn_id__id = id) # don't forget to give the __id after the specified id
            serializer = mst_dev_addr_serializer(devaddr, many = True)
            return Response(serializer.data)
        devaddr = mst_dev_addr.objects.all()
        serializer = mst_dev_addr_serializer(devaddr, many = True)
        return Response(serializer.data)

    def post(self, request,format = None):
        serializer = mst_dev_addr_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Device Address Added Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request,pk=None,format = None):
        id = pk
        devaddr = mst_dev_addr.objects.get(pk=id)
        serializer = mst_dev_addr_serializer(devaddr, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Device Address Updated Successfully'})
        return Response(serializer.errors)

    def delete(self, request,pk,format = None):
        id = pk
        devaddr = mst_dev_addr.objects.get(pk=id)
        devaddr.delete()
        return Response({'Device Address Deleted Successfully'})

class shift_table_API(APIView):
    def get(self, request,ShiftNumber=None,format = None):
        id = ShiftNumber # here we are not taking data by pk instead we use shiftnumber
        if id is not None:
            shift = shift_table.objects.get(id=ShiftNumber)
            serializer = shift_table_serializer(shift)
            return Response(serializer.data)
        shift = shift_table.objects.all()
        serializer = shift_table_serializer(shift, many = True)
        return Response(serializer.data)

    def post(self, request,format = None):
        serializer = shift_table_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Shift Added Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Time formate is, if you want to say 2pm then it must be 14:00:00.000000

    def patch(self, request,pk=None,format = None):
        id = pk
        shift = shift_table.objects.get(pk=id)
        serializer = shift_table_serializer(shift, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Shift Updated Successfully'})
        return Response(serializer.errors)

    def delete(self, request,pk,format = None):
        id = pk
        shift = shift_table.objects.get(pk=id)
        shift.delete()
        return Response({'Shift Address Deleted Successfully'})

class user_level_API(APIView):
    def get(self, request,pk=None,format = None):
        id = pk
        if id is not None:
            userlevel = user_level.objects.get(id=id)
            serializer = user_level_serializer(userlevel)
            return Response(serializer.data)
        userlevel = user_level.objects.all()
        serializer = user_level_serializer(userlevel, many = True)
        return Response(serializer.data)

    def post(self, request,format = None):
        serializer = user_level_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'User Level Added Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request,pk=None,format = None):
        id = pk
        userlevel = user_level.objects.get(pk=id)
        serializer = user_level_serializer(userlevel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'User Level Updated Successfully'})
        return Response(serializer.errors)

    def delete(self, request,pk,format = None):
        id = pk
        userlevel = user_level.objects.get(pk=id)
        userlevel.delete()
        return Response({'User Level Deleted Successfully'})

class user_mng_API(APIView):
    def get(self, request,pk=None,format = None):
        id = pk
        if id is not None:
            usermng = user_mng.objects.get(id=id)
            serializer = user_mng_serializer(usermng)
            return Response(serializer.data)
        usermng = user_mng.objects.all()
        serializer = user_mng_serializer(usermng, many = True)
        return Response(serializer.data)

    def post(self, request,format = None):
        serializer = user_mng_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'User Added Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request,pk=None,format = None):
        id = pk
        usermng = user_mng.objects.get(pk=id)
        serializer = user_mng_serializer(usermng, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'User Updated Successfully'})
        return Response(serializer.errors)

    def delete(self, request,pk,format = None):
        id = pk
        usermng = user_mng.objects.get(pk=id)
        usermng.delete()
        return Response({'User Deleted Successfully'})

# FOR USER MANAGEMENT
# Register API
class RegisterAPI(generics.GenericAPIView): # this api is for registering the user with username and password
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": user_mng_serializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
    
