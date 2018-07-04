import time
import numpy as np
# Import the ADS1x15 module.
import Adafruit_ADS1x15
import cmath
#import matplotlib.pyplot as plt
adc = Adafruit_ADS1x15.ADS1115()
#adc = Adafruit_ADS1x15.ADS1015()
GAIN = 1
dcal=0
adc.start_adc(0, gain=GAIN,data_rate=860)
start = time.time()
while True:
        value=[7000]
        value2=[]

        while( (time.time() - start) <= 1.0):
                                #value=[6000]
                                #value2=[]
                                value = adc.get_last_result()
                                value2.append(value)
                               # print(time.time()-start)
                                #print(value)
   

        #print(value2)
        start=time.time()
        value3=np.array(value2).tolist()
        #print(value3)
        fftv=np.fft.fft(value3)
        Fs=len(value2)/1
        fs=Fs*(np.arange(0,len(value2)))/len(value2)
        k=abs(fftv/len(value3))
        A2L=k.tolist()
        f2l=fs.tolist()

        value2=[0]
        a=(np.where(np.logical_and(fs>44, fs<52)))
        d=(np.where(np.logical_and(fs>64, fs<72)))
        c=(np.where(np.logical_and(fs>110, fs<126)))
        bl=(np.where(np.logical_and(fs>23, fs<26)))
#print(k[b])
        

        #print(max(k[d]))
        #print(max(k[bl]))
        #print(max(k[c]))
        #print(max(k[d]))
        yy=k.tolist()
        ffs=fs.tolist()
        Hg=18
        Pt1=8000
        Pt2=600
        Pt3=5000
        Pt4=7000
        b=np.sqrt(.052*(Hg**2)/3.414)
        Re1=max(k[a])
        Re2=max(k[bl])
        Re3=max(k[c])
        Re4=max(k[d])
##diagonal distance calculation from lambertian law

        d1=b*np.sqrt(Pt1/Re1)
        d2=b*np.sqrt(Pt2/Re2)
        d3=b*np.sqrt(Pt3/Re3)
        d4=b*np.sqrt(Pt4/Re4)
       

        print(d1)
        print(d2)
        print(d3)
        print(d4)

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
                
                

        

        
        
                

