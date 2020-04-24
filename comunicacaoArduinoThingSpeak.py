import serial
import time
import thingspeak

channel_id = 1045992
write_key = 'BKL6E4E9WB492HUG'
ser = serial.Serial('/dev/ttyACM1', 9600)
channel = thingspeak.Channel(id = channel_id, api_key = write_key)
serialcmd = str(chr(116))
while True:
    ser.write(serialcmd.encode())
    time.sleep(1)
    tensao = ser.readline()
    time.sleep(1)
    print(tensao)
    response = channel.update({1:tensao})
    time.sleep(1)
ser.close()    