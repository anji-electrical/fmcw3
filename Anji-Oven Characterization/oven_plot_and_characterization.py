import csv
import matplotlib.pyplot as plt

file_path = 'C:/Users/Lee/Desktop/Oven Characterization/'

csv_unmod0 = open(file_path+'oven_unmodified_0.csv', newline='')
csvreader = csv.reader(csv_unmod0)
i=0
unmod_0=[[],[]]
for row in csvreader:
    if(i>5 and i<600):
        unmod_0[0].append(float(row[0]))
        unmod_0[1].append(float(row[3]))
    i=i+1

csv_glass_foil0 = open(file_path+'oven_glass_foil_0.csv', newline='')
csvreader = csv.reader(csv_glass_foil0)
i=0
glass_foil_0=[[],[]]
for row in csvreader:
    if(i>5 and i<600):
        glass_foil_0[0].append(float(row[0]))
        glass_foil_0[1].append(float(row[3]))
    i=i+1

csv_unmod2 = open(file_path+'oven_unmodified_2.csv', newline='')
csvreader = csv.reader(csv_unmod2)
i=0
unmod_2=[[],[]]
for row in csvreader:
    if(i>5 and i<600):
        unmod_2[0].append(float(row[0]))
        unmod_2[1].append(float(row[3]))
    i=i+1

csv_glass0 = open(file_path+'oven_glass_wool_0.csv', newline='')
csvreader = csv.reader(csv_glass0)
i=0
glass_0=[[],[]]
for row in csvreader:
    if(i>5 and i<600):
        glass_0[0].append(float(row[0]))
        glass_0[1].append(float(row[3]))
    i=i+1
    
#plot
fig,ax=plt.subplots()
ax.plot(unmod_0[0],unmod_0[1],glass_foil_0[0],glass_foil_0[1],glass_0[0],glass_0[1])
plt.show()
