import numpy as np
from sensors import DistanceSensor, TempSensor, ThermalCamera

file = open('file.txt', 'w')

dist = DistanceSensor()
temp = TempSensor()
therm = ThermalCamera()

for _ in range(50):
    d = dist.distance
    t = temp.temp
    th = np.ravel(np.array(therm._amg.pixels))
    file.write(str(d) + ', ' + str(t) + ', [')
    for num in th:
        file.write(str(num) + ' ')
    file.write(']\n')

file.close()
