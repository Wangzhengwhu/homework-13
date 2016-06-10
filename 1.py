from mpl_toolkits.mplot3d import Axes3D  
from matplotlib import cm  
from matplotlib.ticker import LinearLocator, FormatStrFormatter  
import matplotlib.pyplot as plt  
import numpy as np 
import math
#######
da=2.0*math.pi/1000.0
dr=0.01
######
l_1=[]
l_2=[]
B_x=[]
B_y=[]
B_z=[]
B=[]
theta=[0]
x=[0]
y=[0]
z=[]
r=[-1]
######
#for k in range(int(2.0*math.pi/da)):
for j in range(300): 
    s_x=0
    s_y=0
    s_z=0
    l_1=[]
    l_2=[]
    z.append(r[j])
    #x.append(r[j]*math.cos(k*da))
    #y.append(r[j]*math.sin(k*da))
    for i in range(int(2.0*math.pi/da)):
       l_1.append(((x[0]-math.cos(i*da))**2+(y[0]-math.sin(i*da))**2+z[j]**2)**1.5)
       l_2.append(((x[0]-math.cos(i*da))**2+(y[0]-math.sin(i*da))**2+(z[j]-1)**2)**1.5)
       By=(z[j]*math.sin(i*da)/l_1[i]+(z[j]-1)*math.sin(i*da)/l_2[i])*da
       Bx=(z[j]*math.cos(i*da)/l_1[i]+(z[j]-1)*math.cos(i*da)/l_2[i])*da
       Bz=(-math.sin(i*da)*(y[0]-math.sin(i*da))-math.cos(i*da)*(x[0]-math.cos(i*da)))*(1.0/l_1[i]+1.0/l_2[i])*da
       s_x=s_x+Bx
       s_y=s_y+By
       s_z=s_z+Bz
    s=(s_z**2+s_x**2+s_y**2)**0.5
    B_x.append(s_x)
    B_y.append(s_y)
    B_z.append(s_z)
    B.append(s)
    print s
    r.append(r[j]+dr)
##################
#fig = plt.figure()  
#ax = fig.gca(projection='3d')
#X=x
#Y=y
#X,Y=np.meshgrid(X,Y)
#Z=B
#surf=ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=cm.jet,linewidth=0,antialiased=False)  
##ax.set_zlim(-1.01, 1.01)  
#ax.zaxis.set_major_locator(LinearLocator(10))  
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))  
#fig.colorbar(surf, shrink=0.5, aspect=5)  
#plt.show()
##########
plt.plot(z,B)
plt.ylabel(u'B')
plt.xlabel(u'z')
plt.title(u"")
plt.show()