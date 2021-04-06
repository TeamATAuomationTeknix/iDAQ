from django.db import models
import uuid

class mst_dev_conn(models.Model):
    dev_id = models.UUIDField()
    ipAddress = models.CharField(max_length=20)
    portNumber = models.IntegerField()
    plcName = models.CharField(max_length=100)


class units_table(models.Model):
    Unit_id = models.UUIDField()
    unitConversionFactor = models.FloatField()
    unitName = models.CharField(max_length=20)

class mst_dev_addr(models.Model):
    #create plc data addr id and integer type is uuid for unique identification  
    dev_addr_id = models.UUIDField()
    #PlcTcpConnection foreign key. If plcid get deleted from PlcTcpConnection table then all the rows associated with the plcId in the PlcAddress table should be automatically deleted for data consistency
    #To achieve this functionality we have inserted on_delete=models.CASCADE attribute while creating a foreign key
    dev_id = models.ForeignKey(mst_dev_conn,on_delete=models.CASCADE,related_name='DevConnection',default = 0o01)

    unit_id = models.ForeignKey(units_table,on_delete=models.CASCADE)

    #integer field to stre holding reg data
    holdingRegisterNumber = models.IntegerField()

    #to store the total number of registers to be read for collecting data from plc device
    # For example if we are reading an integer the register count is 1 and if we are reading a float value then register count is 2
    ReadRegisterCount = models.SmallIntegerField()

    #To store the type of data INT, FLOAT, DOUBLE ect
    registerType = models.CharField(max_length=10)

    deviceName = models.CharField(max_length=50)
    

class shift_table(models.Model):
    shift_id = models.UUIDField()
    StartShiftTime = models.TimeField()
    EndShiftTime = models.TimeField()
    ShiftNumber = models.IntegerField()

class mst_data(models.Model):
    Data_id = models.UUIDField()
    dev_addr_id = models.ForeignKey(mst_dev_addr,on_delete=models.CASCADE)    
    shift_id = models.ForeignKey(shift_table,on_delete=models.CASCADE)    
    DataValue = models.FloatField()
    AlarmStatus = models.BooleanField()
    DateTime = models.DateTimeField()
    
class user_level(models.Model):
    user_level_id = models.UUIDField()
    LevelName = models.CharField(max_length=30)
    LevelNamePriority = models.SmallIntegerField()

class user_mng(models.Model):
    user_id = models.UUIDField()
    Username = models.CharField(max_length=30)
    PassWord = models.CharField(max_length=10)
    user_level_id = models.ForeignKey(user_level,on_delete=models.CASCADE)
