from .models import mst_dev_conn,units_table,mst_dev_addr,shift_table,mst_data,user_level,user_mng
from .serializers import mst_dev_conn_serializer,units_table_serializer,mst_dev_addr_serializer,shift_table_serializer,mst_data_serializer,user_level_serializer,user_mng_serializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class mst_dev_conn_API(APIView):
    def post(self, request,format = None):
        serializer = mst_dev_conn_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Device Added Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class unit_table_API(APIView):
    def post(self, request,format = None):
        serializer = units_table_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Unit Added Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class mst_dev_addr_API(APIView):
    def post(self, request,format = None):
        serializer = mst_dev_addr_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Device Address Added Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Time formate is, if you want to say 2pm then it must be 14:00:00.000000

class shift_table_API(APIView):
    def post(self, request,format = None):
        serializer = shift_table_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Shift Added Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class user_level_API(APIView):
    def post(self, request,format = None):
        serializer = user_level_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'User Level Added Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class user_mng_API(APIView):
    def post(self, request,format = None):
        serializer = user_mng_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'User Added Successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


