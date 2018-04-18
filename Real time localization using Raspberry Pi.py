import cmath
import numpy as np
#import least square con.py
import matplotlib.pyplot as plt

y=np.fft.fft(H)
k=abs(y)
Fs=len(H)/3
fs=Fs*(np.arange(0,len(H)))/len(H)
a=(np.where(np.logical_and(fs>47, fs<52)))
d=(np.where(np.logical_and(fs>68, fs<72)))
c=(np.where(np.logical_and(fs>121, fs<126)))
bl=(np.where(np.logical_and(fs>145, fs<152)))
#print(k[b])
print(max(k[a]))
print(max(k[bl]))
print(max(k[c]))
print(max(k[d]))
yy=k.tolist()
ffs=fs.tolist()
Hg=18
Pt1=50660
Pt2=49850
Pt3=77890
Pt4=108200
b=np.sqrt(.052*(Hg**2)/3.414)                  #coficent calculation for photodiode

##find received power calculated from photodiode        
Re1=max(k[a])
Re2=max(k[bl])        
Re3=max(k[c])
Re4=max(k[d])
##diagonal distance calculation from lambertian law
                
d1=b*np.sqrt(Pt1/Re1)
d2=b*np.sqrt(Pt2/Re2)
d3=b*np.sqrt(Pt3/Re3)
d4=b*np.sqrt(Pt4/Re4)
# 2d distance calculation

         #d1=sqrt(A1.^2-Hg.^2)
         #d2=sqrt(A2.^2-Hg.^2)
         #d3=sqrt(A3.^2-Hg.^2)
         #d4=sqrt(A4.^2-Hg.^2)
                
##find the intersection point using circle equation
L=[0,0,0,0]
M=[0,0,0,0]
xd=16
yd=16        
y1=(d1**2+yd**2-d2**2)/(2*yd) 
x1=cmath.sqrt(d1**2-y1**2)
L[0]=x1
M[0]=y1
x2=(xd**2-d4**2+d1**2)/(2*xd)
y2=cmath.sqrt(d1**2-x2**2)
L[1]=x2
M[1]=y2
x3=(d2**2-d3**2+xd**2)/(2*xd)
y3=yd-cmath.sqrt(d2**2-x3**2)
L[2]=x3
M[2]=y3
y4=(d4**2-d3**2+yd**2)/(2*yd)
x4=xd-cmath.sqrt(d3**2-(y4-yd)**2)
L[3]=x4
M[3]=y4     
 
X1=[abs(np.mean(L)),abs(np.mean(M))]
print(X1)        
#value2=[0]

#print(len(f2l))
xd=16
yd=16
X=[0,0,xd,xd]
Y=[0,yd,yd,0]
plt.plot(X,Y,'ko')
plt.plot(X1[0],X1[1],'r+')
plt.grid()
x=X1[0]
y=X1[1]
r=3
th=(np.arange(0,2*3.14,0.0328))
xunit = r * np.cos(th)+x 
yunit = r * np.sin(th)+y
plt.plot(xunit, yunit)
plt.show()

