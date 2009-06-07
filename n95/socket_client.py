# Echo client program
import socket
import sensor

HOST = '192.168.1.106'       
PORT = 50007 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

sensor_type = sensor.sensors()['RotSensor']
N95_sensor = sensor.Sensor(sensor_type['id'], sensor_type['category'])
N95_sensor.set_event_filter(sensor.RotEventFilter())

def get_sensor_data (status):
    global direction

    if status == sensor.orientation.TOP:
        direction = 'L'
    elif status == sensor.orientation.LEFT:
        direction = 'F' 
    elif status == sensor.orientation.BOTTOM:
        direction = 'R'
    elif status == sensor.orientation.RIGHT:
        direction = 'Q'

def quit ():
    N95_sensor.disconnect()

N95_sensor.connect (get_sensor_data)

while True:

    if  direction == 'Q':
        break		

    s.send(data)

quit()
s.close()

