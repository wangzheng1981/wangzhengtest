import serial
ser=serial.Serial("com3",38400,timeout=0.5)
print (ser.name)
print (ser.port)
ser.close()
ser.open()

#with open('d:/printer.prn', 'rb') as f:
#    data = f.read()
#ser.write(data)
while True:
   data = ser.readline()
   daa
   if len(data)!=0:
        print (data)
        with open('d:/printer.prn', 'wb') as f:
            f.write(data)
print ('end')
ser.close()
