#y=e^x, n=10
import matplotlib.pyplot as plt
import numpy as np
import math
x=np.linspace(start=0, stop=1, num=10)
y=[0]*10
e=2.718281828459045
m=[0]*4
k=[0]*3
for i in range(10):
    y[i] = e**x[i]

for i in range(4):
    for j in range(10):
        m[i]=m[i]+x[j]**(i+1)
    m[i]=m[i]/10

for i in range(3):
    for j in range(10):
        k[i]=k[i]+(x[j]**(i))*y[j]
    k[i]=k[i]/10
s_11=1
s_12=m[0]
s_13=m[1]
s_22=math.sqrt(math.fabs(m[1]-m[0]**2))
s_23=(m[2]-m[0]*m[1])/s_22
s_33=math.sqrt(math.fabs(m[3]-(m[1]**2+s_23**2)))
z_1=k[0]
z_2=(k[1]-m[0]*k[0])/s_22
z_3=(k[2]-(s_13*z_1+s_23*z_2))/s_33
c_2=z_3/s_33
c_1=(z_2-s_23*c_2)/s_22
c_0=z_1-(s_12*c_1+s_13*c_2)
phi=[0]*10
for i in range(10):
    phi[i]=c_0+c_1*x[i]+c_2*x[i]**2
eps = [0]*10
e_m=0
for i in range(10):
    eps[i]=y[i]-phi[i]
    e_m=e_m+eps[i]**2
Eps=max(eps)
e_m=math.sqrt(e_m/10)
print('e_m=',e_m,'e_max=',Eps)
print('c_0=',c_0,'c_1=',c_1,'c_2=',c_2)
plt.plot(x, y)
plt.plot(x,phi)
plt.show()