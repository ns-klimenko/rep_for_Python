import numpy as np
import matplotlib.pyplot as plt

#  data
x1 = np.arange(0, 195, 15)
x=[]
for i in x1:
    x.append(i)
y = [0, -1, 10, 20, 45, 80, 95, 99, 99, 90, 85, 75, 72] #gps1
y_1 = [0, 8, 10, 36, 66, 90, 99, 100, 112, 105, 90, 91, 97]  #wild type
y_2= [0,4,10,38,72,90,102,100,112,102,90,91,90] #gps2
y_3= [0,8,15,40,64,90,97,100,93,100,90,93,90] #gps3
# error bar values 
error_set_1=[]
for i in range(len(y)):
    if i<5:
        error = i
        error_set_1.append(error)
    else:
        error=10
        error_set_1.append(error)
        
# error bar values 
error_set_2=[]
for i in range(len(y)):
    if i<4:
        error = 1.5*i
        error_set_2.append(error)
    else:
        error=10
        error_set_2.append(error)

plt.errorbar(x, y_1, yerr=error_set_2, fmt="kD-",capsize=3,capthick=0.9, 
             ecolor='k',elinewidth=0.9, linewidth=1.5) #wild type
plt.errorbar(x, y, yerr=error_set_1, fmt="ks-",capsize=3,capthick=0.9, 
             ecolor='k',elinewidth=0.9, linewidth=1.5) #gps1
plt.errorbar(x, y_2, yerr=error_set_2, fmt="k^-",capsize=3,capthick=0.9, 
             ecolor='k',elinewidth=0.9, linewidth=1.5) #gps2
plt.errorbar(x, y_3, yerr=error_set_2, fmt="kx-",capsize=3,capthick=0.9, 
             ecolor='k',elinewidth=0.9, linewidth=1.5)#gps3
plt.xlim([0, 195])
plt.xticks(x)
plt.ylim([-5, 135])
plt.yticks([-5, 15,35,55,75,95,115,135])

WT=plt.plot(x, y_1, "kD-", linewidth=1.5) #wild type
G1=plt.plot(x, y, "ks-", linewidth=1.5) #gps1
G2=plt.plot(x, y_2, "k^-", linewidth=1.5) #gps2
G3=plt.plot(x, y_3, "kx-", linewidth=1.5) #gps3


plt.legend(WT+G1+G2+G3, ['wild type (ws)', ' $gsp1$' ,'$gps2$','$gps3$'],  loc=(0.62, 0.08))
plt.text(5, 125,'B', weight='semibold')
plt.text(180, 125,'RT', weight='semibold')
plt.xlabel('Time (min.)')
plt.ylabel('Angle of Curvature (degrees)')


plt.savefig("/Users/natalaklimenko/Documents/graph1.png",dpi=200)