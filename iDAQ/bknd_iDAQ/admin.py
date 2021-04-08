from django.contrib import admin
from .models import mst_dev_conn, mst_dev_addr, mst_data, units_table, user_level, user_mng, shift_table

# @admin.register(mst_dev_conn)
# class mst_dev_connAdmin(admin.ModelAdmin):
#     list_display = ['dev_id','ipAddress','portNumber','plcName']

# @admin.register(mst_dev_addr)
# class mst_dev_addrAdmin(admin.ModelAdmin):
#     list_display = ['dev_addr_id','dev_id','unit_id','holdingRegisterNumber','ReadRegisterCount','registerType','deviceName']

# @admin.register(mst_data)
# class mst_dataAdmin(admin.ModelAdmin):
#     list_display = ['Data_id','dev_addr_id','shift_id','DataValue','AlarmStatus','DateTime']

# @admin.register(units_table)
# class units_tableAdmin(admin.ModelAdmin):
#     list_display = ['Unit_id','unitConversionFactor','unitName']

# @admin.register(user_level)
# class user_levelAdmin(admin.ModelAdmin):
#     list_display = ['user_level_id','LevelName','LevelNamePriority']

# @admin.register(user_mng)
# class user_mngAdmin(admin.ModelAdmin):
#     list_display = ['user_id','Username','PassWord','user_level_id']

@admin.register(shift_table)
class shift_tableAdmin(admin.ModelAdmin):
    list_display = ['id','StartShiftTime','EndShiftTime','ShiftNumber']

