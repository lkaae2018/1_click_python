from gpiozero import LED, Button
import time

led1=LED(17)
led2=LED(27)
led3=LED(22)
button1=Button(16)
button2=Button(20)
button3=Button(21)
t1=0 #Hvilket state (on(1) eller off(0)) er led1 i!
t2=0 #Hvilket state (on(1) eller off(0)) er led2 i!
t3=0 #Hvilket state (on(1) eller off(0)) er led3 i!
sleep=0.5

while True:
    if button1.is_pressed and t1==0:
        led1.on()
        led2.on()
        led3.on()
        time.sleep(sleep)
        t1=1
       
    elif button2.is_pressed and t1==0:
        led1.on()
        led2.on()
        led3.on()
        time.sleep(sleep)
        t1=1
       
    elif button1.is_pressed and t1==1:
        led1.off()
        led2.off()
        led3.off()
        time.sleep(sleep)
        t1=0
       
    elif button2.is_pressed and t1==1:
        led1.off()
        led2.off()
        led3.off()
        time.sleep(sleep)
        t1=0