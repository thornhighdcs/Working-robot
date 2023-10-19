import time
import board
import digitalio
import pwmio

from adafruit_motor  import motor

left_motor_foward =  board.GP1
left_motor_backward = board.GP2
right_motor_foward =  board.GP12
right_motor_backward = board.GP13

pwm_La = pwmio.PWMOut(left_motor_foward, frequency=10000)
pwm_Lb = pwmio.PWMOut(left_motor_backward, frequency=10000)
pwm_Ra = pwmio.PWMOut(right_motor_foward, frequency=10000)
pwm_Rb = pwmio.PWMOut(right_motor_backward, frequency=10000)

Left_Motor = motor.DCMotor(pwm_La, pwm_Lb)
Left_Motor_speed = 0
right_Motor = motor.DCMotor(pwm_Ra, pwm_Rb)
right_Motor_speed = 0




while True:


    Left_Motor_speed = -1 #Leftfoward
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(4)
    Left_Motor_speed = 1 #Leftbackwards
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(4)

    right_Motor_speed = -1 #rightbackward
    right_Motor.throttle = right_Motor_speed
    time.sleep(4)
    right_Motor_speed = 1 #rightfoward
    right_Motor.throttle = right_Motor_speed
    time.sleep(4)




