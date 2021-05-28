from pyModbusTCP.client import ModbusClient
import time
import threading
import mysql.connector
from datetime import datetime



def driver():
    
    class MySql_unit1:
      
        def getConnection(self):
            
            return mysql.connector.connect(
                host = 'localhost',
                user =  'root',
                password = 'teamat',
                database = 'idaq_database'
            )

        def dataInsert(self,data):
            if 9999 in data:
                now = datetime.now()
                formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
                conn = self.getConnection()
                data = (data)
                Alarm_time=[1,formatted_date]
                All_data = data+Alarm_time
                print("Data receives is ",All_data)
                print('Error')
                cur = conn.cursor()
                s = ("INSERT INTO new_table VALUES (1,%s,%s,%s,%s)")
                cur.execute(s,All_data)
                conn.commit()
                conn.close()
                AlarmStatus = 1
            else:
                now = datetime.now()
                formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
                conn = self.getConnection()
                data = (data)
                Alarm_time=[0,formatted_date]
                All_data = data+Alarm_time
                print("Data receives is ",All_data)
                cur = conn.cursor()
                s = ("INSERT INTO new_table VALUES (1,%s*0.1,%s*0.15,%s,%s)")
                cur.execute(s,All_data)
                conn.commit()
                conn.close()
                AlarmStatus = 0



    def unit1():
        c1 = ModbusClient(host="localhost", port=502, unit_id=1, auto_open=True) #make the unit id and device id in modsim same

        def readData():
            db_addrList = [0,2] 
            # cnt = 6
            resister_addr , count = db_addrList
            data = []
            while(count>0):
                data+=c1.read_holding_registers(resister_addr) #1 
                resister_addr+=1 # 1+1 = 2
                count-=1 # 6-1 =5  5-1 =4....0  
            data+=[] 
            return data

        mySql1 = MySql_unit1()
        milliseconds = int(round(time.time() * 1000))
        while True:
            millisecondsRunning = int(round(time.time() * 1000))
            if (millisecondsRunning-milliseconds) <= 5000 : # this is for 5sec timeframe and we need to implement it for continous loop but with stopping functionality also
                mySql1.dataInsert(readData())
                time.sleep(1)
            else:
                break
    time.sleep(0.01)

    thread_unit1 = threading.Thread(target=unit1)
    thread_unit1.start()