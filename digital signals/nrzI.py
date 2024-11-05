import matplotlib.pyplot as plt
import numpy as np

def toNrzI(dataArray):
    for x in dataArray:
        if dataArray[x] == 0 and dataArray[x+1] == 0:
            continue
        if dataArray[x] == 0 and dataArray[x+1] == 1:
            dataArray[x] = 1
        if dataArray[x] == 1 and dataArray[x+1] == 0:
            continue
        if dataArray[x] == 1 and dataArray[x+1] == 1:
            dataArray[x] = 0
    return dataArray

dataStream1 = [0,1,0,1,1,0,1,1,0,0]
dataStream2 = [1,1,0,0,1,1,0,1,1,0]

toNrzI(dataStream1)
toNrzI(dataStream2)

fig, (ax1, ax2) = plt.subplots(1,2, sharey=False)

# graph 1

strDS1 = ['0','1','0','1','1','0','1','1','0','0']
ax1.step(y=dataStream1, x=np.arange(0,10),where='pre',marker='o', linewidth=2.5)
ax1.set(xlim=(0,len(dataStream1)),ylim=(-0.1,1.1))
ax1.set_xticks(np.arange(0,len(strDS1)), strDS1)
ax1.set_yticks([0,0.5,1], ["-", "0", "+"])
ax1.axhline(y=0.5, c="r")
ax1.set_title("0101101100")
ax1.invert_yaxis()

# graph 2
strDS2 = ['1','1','0','0','1','1','0','1','1','0']
ax2.step(y=dataStream2, x=np.arange(0,10),where='pre',marker='o', linewidth=2.5)
ax2.set(xlim=(0,len(dataStream2)), ylim=(-0.1,1.1))
ax2.set_xticks(np.arange(0,len(strDS2)), strDS2)
ax2.set_yticks([0,0.5,1], ["-", "0", "+"])
ax2.axhline(y=0.5, c="r")
ax2.set_title("1100110110")
ax2.invert_yaxis()


fig.set_size_inches(8,4.5)
fig.suptitle("Data Streams in NRZ-I")
plt.show()
