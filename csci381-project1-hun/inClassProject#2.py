import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# variables
aMax = 1
phase = 0

# calculations
timeAxis = np.arange(0 , 5, 0.05) #start, end, and steps
frequencyAxis = 1 - (aMax * np.sin(np.pi * (timeAxis / 2) + phase))

# plotting
plt.plot(timeAxis, frequencyAxis)
plt.title("f(t) = 1 - sin(pi * t/2)")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.show()
