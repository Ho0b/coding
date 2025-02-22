import matplotlib.pyplot as plt
import numpy as np

def QPSK_Waveform(binaryPair,amp, fc, t):

    offset = 0
    if binaryPair == "00":
        offset = -((3*pi)/4)
    elif binaryPair == "01":
        offset = ((3*pi)/4)
    elif binaryPair == "10":
        offset = -(pi/4)
    elif binaryPair == "11":
        offset = (pi/4)

    carrierSignal = ((2*pi*fc*t) + offset)

    carrierMod = amp * np.cos(carrierSignal)

    return carrierMod

fig, (ax1, ax2, ax3, ax4) = plt.subplots(1,4 , sharey = False)

amplitude = 1
carrierFreq = 4
pi = 3.14159265359
time = np.arange(0, 4, 0.0125)
binaryPairs = ["00", "01", "10", "11"]

graphs = []

for x in binaryPairs:
    print(x)
    y_t = QPSK_Waveform(x, amplitude, carrierFreq, time)
    graphs.append(y_t)


ax1.plot(graphs[0])
ax1.set(ylim=(-2,2))
ax1.set_title(f"b={binaryPairs[0]}")
ax2.plot(graphs[1])
ax2.set(ylim=(-2,2))
ax2.set_title(f"b={binaryPairs[1]}")
ax3.plot(graphs[2])
ax3.set(ylim=(-2,2))
ax3.set_title(f"b={binaryPairs[2]}")
ax4.plot(graphs[3])
ax4.set(ylim=(-2,2))
ax4.set_title(f"b={binaryPairs[3]}")

fig.set_size_inches(16,9)
fig.suptitle("QPSK Waveform")
plt.show()
