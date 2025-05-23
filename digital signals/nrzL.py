import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1,2, sharey=False)

# graph 1

dataStream1 = [0,1,0,1,1,0,1,1,0,0]
strDS1 = [str(i) for i in dataStream1]
ax1.stairs(dataStream1, linewidth=2.5)
ax1.set(xlim=(0,len(dataStream1)),ylim=(0,1.1))
ax1.set_xticks(np.arange(0,10), strDS1)
ax1.set_yticks([0,0.5,1], ["-", "0", "+"])
ax1.axhline(y=0.5, c="r")
ax1.invert_yaxis()
ax1.set_title("0101101100")
ax1.grid(axis="x", linestyle="-")

# graph 2

dataStream2 = [1,1,0,0,1,1,0,1,1,0]
strDS2 = [str(j) for j in dataStream2]
ax2.stairs(dataStream2, linewidth=2.5)
ax2.set(xlim=(0,len(dataStream2)), ylim=(0,1.1))
ax2.set_xticks(np.arange(0,10), strDS2)
ax2.set_yticks([0,0.5,1], ["-", "0", "+"])
ax2.axhline(y=0.5, c="r")
ax2.invert_yaxis()
ax2.set_title("1100110110")
ax2.grid(axis="x", linestyle="-")


fig.set_size_inches(8,4.5)
fig.suptitle("Data Streams in NRZ-L")
plt.show()
