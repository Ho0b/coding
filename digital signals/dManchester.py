import matplotlib.pyplot as plt
import numpy as np

# could not complete, got stuck

def manchesterDouble(dataArray):
    newArray = []
    lastPulse = 0
    if dataArray[0] == 0:
        lastPulse = 1
    else:
        lastPulse = 0

    for x in range(len(dataArray)):
        if dataArray[x] == 0:
            newArray.extend([(1-dataArray[x]), (0+dataArray[x])])
        if dataArray[x] == 1:
            newArray.extend([(1-dataArray[x]), (0+dataArray[x])])
        lastPulse = newArray[x+1]
        print(lastPulse)

    print(dataArray, "original")
    print(newArray)
    return newArray

dataStream1 = [0,1,0,1,1,0,1,1,0,0]
dataStream2 = [1,1,0,0,1,1,0,1,1,0]

manchesterArray1 = manchesterDouble(dataStream1)
manchesterArray2 = manchesterDouble(dataStream2)

fig, (ax1, ax2) = plt.subplots(1,2, sharey=False)

# graph 1
strDS1 = ['0','1','0','1','1','0','1','1','0','0']
ax1.step(y=manchesterArray1, x=np.arange(0,20), where='post', marker='o',markevery=2, linewidth=2.5)
ax1.set(xlim=(0,20),ylim=(-0.75,1.75))
ax1.set_xticks(np.arange(1,20,2), strDS1)
ax1.set_yticks([0,1], ["-", "+"])
ax1.axhline(y=0.5, c="r")
# ax1.grid(axis='x', ls=':', c='0')
ax1.set_title("0101101100")

# graph 2
strDS2 = ['1','1','0','0','1','1','0','1','1','0']
ax2.step(y=manchesterArray2, x=np.arange(0,20), where='post', marker='o',markevery=2, linewidth=2.5)
ax2.set(xlim=(0,20), ylim=(-0.75,1.75))
ax2.set_xticks(np.arange(1,20,2), strDS2)
ax2.set_yticks([0,1], ["-", "+"])
ax2.axhline(y=0.5, c="r")
# ax2.grid(axis='x', ls=':', c='0')
ax2.set_title("1100110110")


fig.set_size_inches(8,4.5)
fig.suptitle("Data Streams in Differential Manchester")
plt.show()
