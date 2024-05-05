'''
Developed by Ellen Red

'''

import machine, time, math
from machine import Pin, I2C
from time import sleep
import imu
from kalman import KalmanAngle
from pidcontroller import PIDController


i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
kalman_x = KalmanAngle()
kalman_y = KalmanAngle()


def acceleration_radius_to_degrees():
    while True:
        radius_to_degrees = 180/3.14159
        accel_x, accel_y, accel_z = imu.mpu6050_get_accel(i2c)
        ax_angle = math.atan(accel_y/math.sqrt(math.pow(accel_x,2) + math.pow(accel_z, 2)))*radius_to_degrees
        ay_angle = math.atan((-1*accel_x)/math.sqrt(math.pow(accel_y,2) + math.pow(accel_z, 2)))*radius_to_degrees
        return ax_angle, ay_angle
    
    
def filter_pid():
    while True:
        t_now = time.ticks_ms()
        last_read_time = 0.0
        dt = (t_now - last_read_time)/1000.0
        
        ax_angle, ay_angle = acceleration_radius_to_degrees()
        gyro_x, gyro_y, gyro_z = imu.mpu6050_get_gyro(i2c)    
    
        k_angle_x = kalman_x.getAngle(ax_angle, gyro_x, dt)
        k_angle_y = kalman_y.getAngle(ay_angle, gyro_y, dt)       
        x, y = k_angle_x, k_angle_y
        newx = x
        newy = y
        PID = PIDController(P=0.2, I=0.02, D=1)
        PIDx = PID.step(newx)
        PIDy = PID.step(newy)        
        result = (k_angle_x, k_angle_y, PIDx, PIDy)
        return(result)

