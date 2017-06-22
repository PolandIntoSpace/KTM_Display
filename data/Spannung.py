import time
spannung = 20
delta = -1
while(1):
        f = open('spannung_vehicle.txt', 'w')
        f.write(str(spannung))
        spannung = spannung + delta
        if (spannung > 20):
            delta = -1
        if (spannung < 0):
            delta = 1
        f.close()
        time.sleep(10)