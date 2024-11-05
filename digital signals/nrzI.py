import matplotlib.pyplot as plt
import numpy as np

def toNrzI(dataArray):
    # note for self:
    inputArray = [0] * len(dataArray) # this makes a new array that allocates the same size of the input array
    currentBit = 0 # this is the previous bit

    for x in range(len(dataArray)): # this loops through each index of the array within the range of the size of the original array size
        if dataArray[x] == 1: # checks if the current index value is 1:
            currentBit = 1 - currentBit #if so it flip flops the value
        inputArray[x] = currentBit # this updates the current index value to the changed bit.
    return inputArray

dataStream1 = [0,1,0,1,1,0,1,1,0,0]
dataStream2 = [1,1,0,0,1,1,0,1,1,0]

changedArray1 = toNrzI(dataStream1)
changedArray2 = toNrzI(dataStream2)

fig, (ax1, ax2) = plt.subplots(1,2, sharey=False)

# graph 1

strDS1 = ['0','1','0','1','1','0','1','1','0','0']
ax1.step(y=changedArray1, x=np.arange(0,10),where='post',marker='o', linewidth=2.5)
ax1.set(xlim=(0,len(dataStream1)),ylim=(-0.1,1.1))
ax1.set_xticks(np.arange(0.5,len(strDS1)), strDS1)
ax1.set_yticks([0,1], ["-", "+"])
ax1.set_title("0101101100")
ax1.invert_yaxis()

# graph 2
strDS2 = ['1','1','0','0','1','1','0','1','1','0']
ax2.step(y=changedArray2, x=np.arange(0,10),where='post',marker='o', linewidth=2.5)
ax2.set(xlim=(0,len(dataStream2)), ylim=(-0.1,1.1))
ax2.set_xticks(np.arange(0.5,len(strDS2)), strDS2)
ax2.set_yticks([0,1], ["-", "+"])
ax2.set_title("1100110110")
ax2.invert_yaxis()


fig.set_size_inches(8,4.5)
fig.suptitle("Data Streams in NRZ-I")
plt.show()
