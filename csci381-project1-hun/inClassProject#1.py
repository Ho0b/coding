import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# variables
pi = np.pi
aMax = 1
phase = 0

# calculations
timeAxis = np.arange(0 , 5, 0.05) #start, end, and steps
frequencyAxis = aMax * np.sin(np.pi * timeAxis + phase)

# plotting
plt.plot(timeAxis, frequencyAxis)
plt.title("f(t) = sin(pi * t)")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.show()
