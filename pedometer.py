from matplotlib import pyplot as plt
import pandas as pd
from scipy.signal import find_peaks_cwt
import numpy as np

columns = ["Time","Sensor1","Sensor2","Sensor3"]
accelerometer = pd.read_csv("reps.csv", usecols=columns)

data = np.array(accelerometer.Sensor1)
peaks = find_peaks_cwt(data, widths=np.ones(data.shape)*2)-1
plt.plot(data)

plt.plot(peaks, data[peaks], "x")



plt.show()


