import time
speed = 0
delta = 1
while(1):
        f = open('/home/pi/KTM_Display/data/speed_vehicle.txt', 'w')
        f.write(str(speed))
        speed = speed + delta
        if (speed > 20):
            delta = -0.5
        if (speed < -5):
            delta = 0.5
        f.close()
        time.sleep(0.5)
