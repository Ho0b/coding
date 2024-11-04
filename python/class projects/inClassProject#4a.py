import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# variables
aMax = (4/np.pi)
phase = 0

# calculations
timeAxis = np.arange(0 , 5, 0.05) #start, end, and steps
frequencyAxis = (aMax * np.sin((2*np.pi) * timeAxis + phase))

# plotting
plt.plot(timeAxis, frequencyAxis)
plt.title("f(t) = 4/pi * sin(2pi * t)")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.show()
