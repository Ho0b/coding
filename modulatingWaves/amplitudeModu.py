import matplotlib.pyplot as plt
import numpy as np

def AM_Modulation(amp, fc, fm, mi, t):
    envelope = 1 + mi
    carrierSignal = amp * np.sin(2 * pi * fc * t)
    modSignal = envelope * np.cos(2 * pi * fm * t)
    return modSignal * carrierSignal

fig, (ax1, ax2, ax3) = plt.subplots(1,3 , sharey = False)

amplitude = 1
carrierFreq = 4
modFreq = 1
modIndex = [0.75, 0.4, 0.1]
pi = 3.14159265359
time = np.arange(0, 2, 0.005)

graphs = []

for m in modIndex:
    print(m)
    y_t = AM_Modulation(amplitude, carrierFreq, modFreq, m, time)
    graphs.append(y_t)

ax1.plot(graphs[0])
ax1.set(ylim=(-2,2))
ax1.set_title("modulation index 0.75")
ax2.plot(graphs[1])
ax2.set(ylim=(-2,2))
ax2.set_title("modulation index 0.4")
ax3.plot(graphs[2])
ax3.set(ylim=(-2,2))
ax3.set_title("modulation index 0.1")

fig.set_size_inches(16,9)
fig.suptitle("AM modulation")
plt.show()
