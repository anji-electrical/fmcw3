import time
import pyvisa
import serial
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

#make pyvisa resource manager object
#use it to initialize DMM 
rm=pyvisa.ResourceManager()
NameString = rm.list_resources()[1]
DMM = rm.open_resource(NameString)
#print the identity of DMM to make sure we have the correct device
print(DMM.query('*IDN?'))

#initial data and creating the first plot and frame
x=[1]
y=[float(DMM.query('FETC?'))] #get the current meter reading
fig, ax = plt.subplots()
graph = ax.plot(x,y,color = 'g')[0]

ser = serial.Serial('COM11')
kp = 0.3
ki = 0.1
kd = 4
e = [10]
on = bytes('n','UTF-8')
off = bytes('f','UTF-8')

#updates the data and graph
def update(frame):
    global graph

    #x stores index
    x.append(x[-1] + 1)
    
    if(x[-1]<90):
        target=90
    elif(x[-1]>=90 and x[-1]<180):
        target=120
    elif(x[-1]>=180 and x[-1]<240):
        target=165
    else:
        target=0
    #take current temperature
    current_temperature = float(DMM.query('FETC?'))
    # updating the data
    y.append(current_temperature)
    e.append(target-current_temperature)

    p=kp*e[-1]
    if(x[-1]>10):
        i=kp*sum(e[-10:0:])
    else:
        i=kp*sum(e)
    d=kd*(e[-1]-e[-2])
    u=p+i+d
    print(u)
    if(u>0):
        ser.write(on)
    else:
        ser.write(off)
    
    # creating a new graph or updating the graph
    graph.set_xdata(x)
    graph.set_ydata(y)
    plt.xlim(x[0], x[-1])
    plt.ylim(min(y),max(y))
    time.sleep(1)

anim = FuncAnimation(fig, update, frames = None)
plt.show()
