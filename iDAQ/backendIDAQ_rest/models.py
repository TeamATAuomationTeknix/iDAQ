from django.db import models

# Create your models here.
class PlcTcpConnection(models.Model):
    ipAddress = models.CharField(max_length=20)
    portNumber = models.IntegerField()
    plcName = models.CharField(max_length=100)


class UnitTable(models.Model):
    unitName = models.CharField(max_length=20)
    unitConversionFactor = models.FloatField()

class PlcAddress(models.Model):
    #create plc data addr id and integer type is uuid for unique identification  

    #PlcTcpConnection foreign key. If plcid get deleted from PlcTcpConnection table then all the rows associated with the plcId in the PlcAddress table should be automatically deleted for data consistency
    #To achieve this functionality we have inserted on_delete=models.CASCADE attribute while creating a foreign key
    plcID = models.ForeignKey(PlcTcpConnection,on_delete=models.CASCADE,related_name='PlcConnection')

    #unitID = models.ForeignKey(UnitTable,on_delete=models.CASCADE)

    #integer field to stre holding reg data
    holdingRegisterNumber = models.IntegerField()

    #to store the total number of registers to be read for collecting data from plc device
    # For example if we are reading an integer the register count is 1 and if we are reading a float value then register count is 2
    ReadRegisterCount = models.SmallIntegerField()

    #To store the type of data INT, FLOAT, DOUBLE ect
    registerType = models.CharField(max_length=10)

    deviceName = models.CharField(max_length=50)
    

class ShiftTable(models.Model):
    StartShiftTime = models.TimeField()
    EndShiftTime = models.TimeField()
    ShiftNumber = models.IntegerField()

class DataTable(models.Model):
    DataID = models.UUIDField(primary_key=True)
    plcDataAddrID = models.ForeignKey(PlcAddress,on_delete=models.CASCADE)    
    ShiftID = models.ForeignKey(ShiftTable,on_delete=models.CASCADE)    
    DataValue = models.FloatField()
    AlarmStatus = models.BooleanField()
    DateTime = models.DateTimeField()
    
class UserLevel(models.Model):
    LevelName = models.CharField(max_length=30)
    LevelNamePriority = models.SmallIntegerField()

class UserManagement(models.Model):
    Username = models.CharField(max_length=30)
    PassWord = models.CharField(max_length=10)
    UserLevelID = models.ForeignKey(UserLevel,on_delete=models.CASCADE)

