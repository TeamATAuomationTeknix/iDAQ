from pymodbus.client.sync import ModbusTcpClient

Ip_Address = '127.0.0.1'
# port = 1
client = ModbusTcpClient(Ip_Address)

print(client.connect())

# client.write_register(0,55)
# client.write_register(1,99)
# client.write_register(2,77)
# client.write_register(3,0)
# client.write_register(4,0)
# client.write_register(5,0)


result = client.read_holding_registers(0,100)
print('%MW0 : ' + str(result.registers[0]))
print('%MW1 : ' + str(result.registers[1]))
# print('%MW2 or Flow Meter : ' + str(result.registers[2]))
# print('%MW3 : ' + str(result.registers[3]))
# print('%MW4 or Temp Meter : ' + str(result.registers[4]))
# print('%MW5 : ' + str(result.registers[5]))
# print('%MW6 : ' + str(result.registers[100]))

# result = client.read_holding_registers(0,2)
# print('MW6 is: ' + str(result.registers[6]))
count = 0
from pymodbus.payload import BinaryPayloadDecoder

from pymodbus.constants import Endian
# MF0
# mw0 and mw1
# |1|2|3|4| byte ordering big = left to right store
# |w1|w0| word ordering


while count<=20:
    result = client.read_holding_registers(count,2)
    decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big, wordorder=Endian.Little)
    print(decoder.decode_32bit_float())
    count+=2

# count = 0
# while count <10:
#     print('MF3 is: ' + str(result.registers[count]))

#     count+=1
#
# print('MF3 is: ' + str(result.registers[1]))
# print('MF3 is: ' + str(result.registers[2]))
# print('MF3 is: ' + str(result.registers[3]))
# count = 0
# import time
# milliseconds = int(round(time.time() * 1000))
# while True:
#     millisecondsRunning = int(round(time.time() * 1000))
#     if (millisecondsRunning-milliseconds) < 10000 :
#         result = client.read_holding_registers(0, 100)
#         print('%MW2 0r Flow Meter : ' + str(result.registers[2]))
#     else:
#         break
