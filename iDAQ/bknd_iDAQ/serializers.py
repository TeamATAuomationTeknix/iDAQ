from rest_framework import serializers
from .models import mst_dev_conn, mst_dev_addr, mst_data, units_table, user_level, user_mng, shift_table
from django.contrib.auth.models import User


class mst_dev_conn_serializer(serializers.ModelSerializer):
    class Meta:
        model = mst_dev_conn
        fields = ['id','ipAddress','portNumber','deviceName']

class units_table_serializer(serializers.ModelSerializer):
    class Meta:
        model = units_table
        fields = ['id','unitConversionFactor','unitName']

class mst_dev_addr_serializer(serializers.ModelSerializer):
    class Meta:
        model = mst_dev_addr
        fields = ['id','mst_dev_conn_id','units_table_id','holdingRegisterNumber','ReadRegisterCount','registerType','fieldDeviceName']

class shift_table_serializer(serializers.ModelSerializer):
    class Meta:
        model = shift_table
        fields = ['id','StartShiftTime','EndShiftTime','ShiftNumber']

class mst_data_serializer(serializers.ModelSerializer):
    class Meta:
        model = mst_data
        fields = ['id','mst_dev_addr_id','shift_table_id','DataValue','AlarmStatus','DateTime']

class user_level_serializer(serializers.ModelSerializer):
    class Meta:
        model = user_level
        fields = ['id','LevelName','LevelNamePriority']

class user_mng_serializer(serializers.ModelSerializer):
    class Meta:
        model = user_mng
        fields = ['id','user_level_id','Username','email']

    
# class user_mng_serial(serializers.ModelSerializer):   FROM MVMcQCR
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','user_level_id', 'username', 'email','password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
