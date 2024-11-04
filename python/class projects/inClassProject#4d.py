import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# variables
aMax1 = (4/np.pi)

seriesSum = 0

# calculations
timeAxis = np.arange(0 , 5, 0.005) #start, end, and steps

n = 1
while n <= 25:
    if n % 2 != 0:
        frequencyAxis = (aMax1 *
                            ( (1/n) * np.sin(2 * n * np.pi * timeAxis) ) )
        print(frequencyAxis)
        print("iteration #", n)
        seriesSum += frequencyAxis
    n += 1

# plotting
plt.plot(timeAxis, seriesSum)
plt.title("Sigma of f(t) = 4/pi ( (1/n) * sin(2 * n * pi * t) ) , n max = 25, n = odd")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")
plt.show()
