import numpy as np
import matplotlib.pyplot as plt

binaryArray = [0,1,0,1,1,0,1,1,0,0]

# graphing

fig, ax = plt.subplots()

ax.set_title("Data: 0101101100")
ax.set_ylabel("Voltage: - & +")
ax.set_xlabel("Binaries")
ax.stairs(binaryArray, linewidth=2)


ax.set(xlim=(0, len(binaryArray)),
        xticks=(np.arange(0,len(binaryArray))),
        ylim=(0, 2),
        yticks=np.arange(0, 2))

plt.grid(True)
plt.show()
