import matplotlib.pyplot as plt
import numpy as np

def manchesterDouble(dataArray):
    newArray = []
    for x in dataArray:
        newArray.extend([x,1-x])
    print(newArray)
    return newArray

dataStream1 = [0,1,0,1,1,0,1,1,0,0]
dataStream2 = [1,1,0,0,1,1,0,1,1,0]

manchesterArray1 = manchesterDouble(dataStream1)
manchesterArray2 = manchesterDouble(dataStream2)

fig, (ax1, ax2) = plt.subplots(1,2, sharey=False)

# graph 1
strDS1 = ['0','1','0','1','1','0','1','1','0','0']
ax1.step(y=manchesterArray1, x=np.arange(0,20), where='pre', linewidth=2.5)
ax1.set(xlim=(0,20),ylim=(-0.75,1.75))
ax1.set_xticks(np.arange(1,20,2), strDS1)
ax1.set_yticks([0,1], ["-", "+"])
ax1.axhline(y=0.5, c="r")
ax1.grid(axis='x', ls=':', c='0')
ax1.set_title("0101101100")

# graph 2
strDS2 = ['1','1','0','0','1','1','0','1','1','0']
ax2.step(y=manchesterArray2, x=np.arange(0,20), where='pre', linewidth=2.5)
ax2.set(xlim=(0,20), ylim=(-0.75,1.75))
ax2.set_xticks(np.arange(1,20,2), strDS2)
ax2.set_yticks([0,1], ["-", "+"])
ax2.axhline(y=0.5, c="r")
ax2.grid(axis='x', ls=':', c='0')
ax2.set_title("1100110110")


fig.set_size_inches(8,4.5)
fig.suptitle("Data Streams in Manchester")
plt.show()
