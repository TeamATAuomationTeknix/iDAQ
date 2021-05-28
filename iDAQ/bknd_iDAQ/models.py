from django.db import models

class mst_dev_conn(models.Model):
    id = models.AutoField(auto_created = True,primary_key = True,serialize = False, verbose_name ='ID')
    ipAddress = models.CharField(max_length=20)
    portNumber = models.IntegerField()
    deviceName = models.CharField(max_length=100)


class units_table(models.Model):
    id = models.AutoField(auto_created = True,primary_key = True,serialize = False, verbose_name ='ID')
    unitConversionFactor = models.FloatField()
    unitName = models.CharField(max_length=20)

class mst_dev_addr(models.Model):
    id = models.AutoField(auto_created = True,primary_key = True,serialize = False, verbose_name ='ID')
    mst_dev_conn_id = models.ForeignKey(mst_dev_conn, on_delete=models.CASCADE)
    units_table_id = models.ForeignKey(units_table, on_delete=models.CASCADE)
    holdingRegisterNumber = models.IntegerField()
    ReadRegisterCount = models.SmallIntegerField()
    registerType = models.CharField(max_length=10)
    fieldDeviceName = models.CharField(max_length=50)
        

class shift_table(models.Model):
    id = models.AutoField(auto_created = True,primary_key = True,serialize = False, verbose_name ='ID')
    StartShiftTime = models.TimeField()
    EndShiftTime = models.TimeField()
    ShiftNumber = models.IntegerField()
# Time formate is, if you want to say 2pm then it must be 14:00:00.000000


class mst_data(models.Model):
    id = models.AutoField(auto_created = True,primary_key = True,serialize = False, verbose_name ='ID')
    mst_dev_addr_id = models.ForeignKey(mst_dev_addr, on_delete=models.CASCADE)
    shift_table_id = models.ForeignKey(shift_table, on_delete=models.CASCADE)
    DataValue = models.FloatField()
    AlarmStatus = models.BooleanField()
    DateTime = models.DateTimeField()
    
class user_level(models.Model):
    id = models.AutoField(auto_created = True,primary_key = True,serialize = False, verbose_name ='ID')
    LevelName = models.CharField(max_length=30)
    LevelNamePriority = models.SmallIntegerField()

class user_mng(models.Model):
    id = models.AutoField(auto_created = True,primary_key = True,serialize = False, verbose_name ='ID')
    user_level_id = models.ForeignKey(user_level, on_delete=models.CASCADE)
    Username = models.CharField(max_length=30)
    PassWord = models.CharField(max_length=10)




