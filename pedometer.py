from matplotlib import pyplot as plt

import pandas as pd

columns = ["Time","Sensor1","Sensor2","Sensor3"]
accelerometer = pd.read_csv("accelerometer1.csv", usecols=columns)

plt.plot(accelerometer.Time, accelerometer.Sensor1)
plt.plot(accelerometer.Time, accelerometer.Sensor2)
plt.plot(accelerometer.Time, accelerometer.Sensor3)



plt.show()


