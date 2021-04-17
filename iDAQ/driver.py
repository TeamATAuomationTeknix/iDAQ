from pymodbus.client.sync import ModbusTcpClient
class DriverPlc:
    ipAddr = ''
    portNo = ''
    plcName = ''


    def connectToPlc(self,data):

        for singleData in data:
            print(singleData)

data = [['192.168.0.1','101','name1'],['192.168.0.2','102','name2'],['192.168.0.3','103','name3']]        

plc1 = DriverPlc() 

plc1.connectToPlc(data)