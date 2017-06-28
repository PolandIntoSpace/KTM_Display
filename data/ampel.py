import time
times = 20
red = '"RED"}'
green = '"GREEN"}'
phase = red
while(1):
        f = open('/home/pi/KTM_Display/data/status_ampel.json', 'w')
        f.write('{"seconds": ')
        f.write(str(times))
        f.write(', "phase": ')
        f.write(phase)
        f.write('\n')
        times = times -1
        if (times < 1):
            times = 20
            if (phase == red):
                phase = green
            else:
                phase = red
        f.close()
        time.sleep(1)
