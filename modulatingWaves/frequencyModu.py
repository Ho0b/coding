import matplotlib.pyplot as plt
import numpy as np

def FM_Modulation(amp, fc, fm, bi, t):
    inputModPhase = 2 * pi * fc * t
    inputSignal = bi * np.sin(2 * pi * fm * t)
    inputPhasePlusSignal = inputModPhase + inputSignal
    carrierMod = amp * np.cos(inputPhasePlusSignal)
    return carrierMod

fig, (ax1, ax2, ax3) = plt.subplots(1,3 , sharey = False)

amplitude = 1
carrierFreq = 4
modFreq = 1
bIndex = [1.0, 0.5, 2.0]
pi = 3.14159265359
time = np.arange(0, 2, 0.0125)

graphs = []

for m in bIndex:
    print(m)
    y_t = FM_Modulation(amplitude, carrierFreq, modFreq, m, time)
    graphs.append(y_t)


ax1.plot(graphs[0])
ax1.set(ylim=(-2,2))
ax1.set_title("modulation index 0.75")
ax2.plot(graphs[1])
ax2.set(ylim=(-2,2))
ax2.set_title("modulation index 0.45")
ax3.plot(graphs[2])
ax3.set(ylim=(-2,2))
ax3.set_title("modulation index 2")

fig.set_size_inches(16,9)
fig.suptitle("FM modulation")
plt.show()
