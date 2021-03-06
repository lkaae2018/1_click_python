from gpiozero import LED, Button
import time

led=LED(13)
led1=LED(19)
button= Button(16)
button1= Button(20)
t1=0 #Hvilket state (on(1) eller off(0)) er led i!
t2=0 #Hvilket state (on(1) eller off(0)) er led1 i!
sleep=0.5

def tænd(t1,t2):
    while True:
        if button.is_pressed and t1==0:
            led.on()
            time.sleep(sleep)
            t1=1
            return sluk(t1,t2)
        elif button1.is_pressed and t2==0:
            led1.on()
            time.sleep(sleep)
            t2=1
            return sluk(t1,t2)
        elif button.is_pressed and t1==1:
            led.off()
            time.sleep(sleep)
            t1=0
            return tænd(t1,t2)
        elif button1.is_pressed and t2==1:
            led1.off()
            time.sleep(sleep)
            t2=0
            return tænd(t1,t2)
    
def sluk(t1,t2):
    while True:
        if button.is_pressed and t1==1:
            led.off()
            time.sleep(sleep)
            t1=0
            return tænd(t1,t2)
        elif button1.is_pressed:
            led1.off()
            time.sleep(sleep)
            t2=0
            return tænd(t1,t2)
        elif button.is_pressed and t1==0:
            led.on()
            time.sleep(sleep)
            t1=1
            return sluk(t1,t2)
        elif button1.is_pressed and t2==0:
            led1.on()
            time.sleep(sleep)
            t2=1
            return sluk(t1,t2)
    
state=tænd(t1,t2)
while state: state=state()
print("Færdig")