import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# variables
aMax1 = (4/np.pi)
aMax2 = (1/3)

# calculations
timeAxis = np.arange(0 , 5, 0.05) #start, end, and steps
frequencyAxis = (aMax1 *
                    (np.sin(2*np.pi * timeAxis) ) +
                (aMax2 *
                    (np.sin(6*np.pi * timeAxis) )
                )
                )

# plotting
plt.plot(timeAxis, frequencyAxis)
plt.title("f(t) = 4/pi*sin(2pi * t) + 1/3*sin(6pi * t)")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.show()
