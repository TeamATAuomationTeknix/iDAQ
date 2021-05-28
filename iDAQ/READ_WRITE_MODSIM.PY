# https://pypi.org/project/pyModbusTCP/
from pyModbusTCP.client import ModbusClient
import time
import mysql.connector
from connector import MySql

c = ModbusClient(host="localhost", port=502, unit_id=1, auto_open=True) #make the unit id and device id in modsim same
# c = ModbusClient()
# c.host("localhost")
# c.port(502)
# c.unit_id(1)
# c.open()

def readData():
    db_addrList = [0,6] 
    # cnt = 6
    resister_addr , count = db_addrList
    data = []
    while(count>0):
        data+=c.read_holding_registers(resister_addr) #1 
        resister_addr+=1 # 1+1 = 2
        count-=1 # 6-1 =5  5-1 =4....0  
    data+=[] 
    return data
# a = c.read_holding_registers(1)
# b = c.read_holding_registers(1)
# c1 = c.read_holding_registers(2)
# d = c.read_holding_registers(3)
# e = c.read_holding_registers(4)
# f = c.read_holding_registers(5)
# regs = c.read_holding_registers(0)
# regs1 = c.read_holding_registers(7)
# if regs:
#     print(regs)
# else:
#     print("read error")

mySql = MySql()
milliseconds = int(round(time.time() * 1000))
while True:
    millisecondsRunning = int(round(time.time() * 1000))
    if (millisecondsRunning-milliseconds) <= 5000 : # this is for 5sec timeframe and we need to implement it for continous loop but with stopping functionality also
        # regs = a
        # regs1 = b
        # regs2 = c1
        # regs3 = d
        # regs4 = e
        # regs5 = f
        # print('40001 : {}'.format(regs))
        # print('40002 : {}'.format(regs1))
        # print('40003 : {}'.format(regs2))
        # print('40004 : {}'.format(regs3))
        # print('40005 : {}'.format(regs4))
        # print('40006 : {}'.format(regs5))
        mySql.dataInsert(tuple(readData()))
        time.sleep(1)
    else:
        break

