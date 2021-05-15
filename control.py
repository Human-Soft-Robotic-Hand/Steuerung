import machine
import utime

valve_finger_close = machine.Pin(16, machine.Pin.OUT)
valve_finger_open = machine.Pin(18, machine.Pin.OUT)
led_red = machine.Pin(21, machine.Pin.OUT)
pin_r_analog = machine.ADC(28)
pressed = 0

#button_green = Pin(11, Pin.IN, Pin.PULL_DOWN)
#button_yellow = Pin(12, Pin.IN, Pin.PULL_DOWN)
#button_red = Pin(13, Pin.IN, Pin.PULL_DOWN)

#valve_finger_close.value(0)  

  
while pressed == 0:
    r_analog = pin_r_analog.read_u16()
    
    if r_analog > 50000:
        pressed = 1
        valve_finger_close.value(1)
        utime.sleep(5)
        valve_finger_close.value(0)
        utime.sleep(10) 
        valve_finger_open.value(1)
        utime.sleep(5)
        valve_finger_open.value(0)