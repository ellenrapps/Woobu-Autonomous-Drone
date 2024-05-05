'''
Developed by Ellen Red

'''

from machine import Pin, PWM
import time
import imu
import kalman_pid


motor1 = PWM(Pin(22))
motor2 = PWM(Pin(18))
motor3 = PWM(Pin(12))
motor4 = PWM(Pin(4))
freq = 30
duty_u16 = 0


#5%
def slow():
    motor1.duty_u16(3251)
    motor2.duty_u16(3251)
    motor3.duty_u16(3251)
    motor4.duty_u16(3251)
    

#90%
def high():
    motor1.duty_u16(58522)
    motor2.duty_u16(58522)
    motor3.duty_u16(58522)
    motor4.duty_u16(58522)


#50%
def hover():
    motor1.duty_u16(32512)
    motor2.duty_u16(32512)
    motor3.duty_u16(32512)
    motor4.duty_u16(32512)    
   
   
#0%
def off():
    motor1.duty_u16(0)
    motor2.duty_u16(0)
    motor3.duty_u16(0)
    motor4.duty_u16(0)


def auto_takeoff_button():
    start = time.ticks_ms()    
    while True:
        values_kalman_pid = kalman_pid.filter_pid()
        pid_x = values_kalman_pid[2]
        pid_y = values_kalman_pid[3]
        
        if -4 <= pid_x <= 1 and -6 <= pid_y <= 1:            
            high()            
            print('Up High Plain')
            
            if time.ticks_diff(time.ticks_ms(), start) > 200:
                hover()
                print('Hover High Time')
                break
            
        else:
            hover()
            print('Up High Hover Else')
            break        

def hover_button():
    hover()
    print('Hover')
    

def down_button():
    start = time.ticks_ms()
    while True:
        values_kalman_pid = kalman_pid.filter_pid()
        pid_x = values_kalman_pid[2]
        pid_y = values_kalman_pid[3]
        
        if -4 <= pid_x <= 1 and -6 <= pid_y <= 1:            
            slow()
            print('Down Plain')
            
            if time.ticks_diff(time.ticks_ms(), start) > 200:
                off()
                print('Down Off Time')
                break
            
        else:
            hover()
            print('Down Hover Else')
            break        


def on_manual_button():
    slow()
    print('On')
    

def off_manual_button():
    off()
    print('Off')

