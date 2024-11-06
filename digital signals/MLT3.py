import matplotlib.pyplot as plt
import numpy as np

def toMlt3(dataArray):
    newArray = [] * 10
    currentState = None
    currentVoltage = None
    states = [1.0, 0.5, 0.0] #positive 1, 0 0.5, negative 0 on yaxis

    if dataArray[0] == 0:
        currentState = states[0] #if first bit is 0, positive state
        currentVoltage = 1
    else:
        currentState = states[2] #if first bit is not 0, negative state
        currentVoltage = -1

    for x in range(len(dataArray)):
        if currentState == 0 and dataArray[x] == 0: #if negative and nextbit is 0, stay
            currentState = states[2] # negative volt
        elif currentState == 0 and dataArray[x] == 1: #if negative and nextbit is 1, change to zero
            currentState = states[1] # zero
            currentVoltage = -1
        elif currentState == 0.5 and dataArray[x] == 0: #if at 0 and nextbit is 0, stay
            currentState = states[1] # zero
        elif currentState == 0.5 and dataArray[x] == 1: #if at 0 and nextbit is 1, opposite of last non zero
            currentVoltage *= -1
            if currentVoltage == -1: #if last voltage is positive
                currentState = states[2] # negative
                currentVoltage = -1
            else:
                currentState = states[0] # positive
                currentVoltage = 1
        elif currentState == 1 and dataArray[x] == 0: #if posititve and nextbit is 0, stay
            currentState = states[0]
        elif currentState == 1 and dataArray[x] == 1: #if positive and nextbit is 1, change to zero
            currentState = states[1]
            currentVoltage = 1

        newArray.append(currentState)

    print(dataArray, "original")
    print(newArray)
    return newArray

dataStream1 = [0.0,1.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0,0.0]
dataStream2 = [1.0,1.0,0.0,0.0,1.0,1.0,0.0,1.0,1.0,0.0]

convertedMlt3_1 = toMlt3(dataStream1)
convertedMlt3_2 = toMlt3(dataStream2)

fig, (ax1, ax2) = plt.subplots(1,2, sharey=False)

# graph 1
strDS1 = ['0','1','0','1','1','0','1','1','0','0']
ax1.step(y=convertedMlt3_1, x=np.arange(0,10), where='post', marker='o',markevery=2, linewidth=2.5)
ax1.set(xlim=(0,10),ylim=(-0.75,1.75))
ax1.set_xticks(np.arange(0,10), strDS1)
ax1.set_yticks([0,0.5,1], ["-", '0', "+"])
ax1.axhline(y=0.5, c="r")
# ax1.grid(axis='x', ls=':', c='0')
ax1.set_title("0101101100")

# graph 2
strDS2 = ['1','1','0','0','1','1','0','1','1','0']
ax2.step(y=convertedMlt3_2, x=np.arange(0,10), where='post', marker='o',markevery=2, linewidth=2.5)
ax2.set(xlim=(0,10), ylim=(-0.75,1.75))
ax2.set_xticks(np.arange(0.5,10), strDS2)
ax2.set_yticks([0,0.5,1], ["-",'0', "+"])
ax2.axhline(y=0.5, c="r")
# ax2.grid(axis='x', ls=':', c='0')
ax2.set_title("1100110110")


fig.set_size_inches(8,4.5)
fig.suptitle("Data Streams in MLT-3")
plt.show()
