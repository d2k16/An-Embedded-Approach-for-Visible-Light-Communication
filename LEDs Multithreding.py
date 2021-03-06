### The program illustrates the frequency generation using the LED. The concept of multithreding is used for parallel execuion of loop. 


import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

GPIO.setwarnings(False)

# generate the 50Hz 
def led1():
        while True:
                GPIO.output(7,True)
                time.sleep(0.01)
                GPIO.output(7,False)
                time.sleep(0.01)

def led2():
          while True:
               GPIO.output(11,True)
               time.sleep(.007)
               GPIO.output(11,False)
               time.sleep(.007)
#generate the 125hz
def led3():
          while True:
               GPIO.output(13,True)
               time.sleep(.004)
               GPIO.output(13,False)
               time.sleep(.004)
               
#generate the 146.7Hz
def led4():
          while True:
               GPIO.output(15,True)
               time.sleep(.00334)
               GPIO.output(15,False)
               time.sleep(.00334)

t1=threading.Thread(target=led1,args=())
t2=threading.Thread(target=led2,args=())
t3=threading.Thread(target=led3,args=())
t4=threading.Thread(target=led4,args=())
t1.start()
t2.start()
t3.start()
t4.start()
