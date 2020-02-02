###################
# 逻辑:
# 启动调用初始化程序，开始直线行进
# 左转/右转时，对应马达停转数秒，然后停止行进
# 停止行进时，不stop，而是仅将速度设为0
# 加速/减速时改变一定速度值
###################

import RPi.GPIO as GPIO
import time

# left
L_Motor = None
PWM_A = 21
AIN1 = 6
AIN2 = 13
# right
R_Motor = None
PWM_B = 20
BIN1 = 26
BIN2 = 19
# parameter
speed = 50
time_stop = 2
direction_state = 1


# 初始化,自动调用前进
def start():
    global L_Motor
    global R_Motor
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(AIN2, GPIO.OUT)
    GPIO.setup(AIN1, GPIO.OUT)
    GPIO.setup(PWM_A, GPIO.OUT)

    GPIO.setup(BIN1, GPIO.OUT)
    GPIO.setup(BIN2, GPIO.OUT)
    GPIO.setup(PWM_B, GPIO.OUT)

    L_Motor = GPIO.PWM(PWM_A, 100)
    L_Motor.start(0)

    R_Motor = GPIO.PWM(PWM_B, 100)
    R_Motor.start(0)

    # cmd_up()


# 前进
def cmd_up():
    global direction_state
    direction_state = 1
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, False)  # AIN2
    GPIO.output(AIN1, True)  # AIN1

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, False)  # BIN2
    GPIO.output(BIN1, True)  # BIN1


# 后退
def cmd_down():
    global direction_state
    direction_state = 0
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(AIN2, True)  # AIN2
    GPIO.output(AIN1, False)  # AIN1

    R_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN2, True)  # BIN2
    GPIO.output(BIN1, False)  # BIN1


# 停止
def cmd_stop():
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(AIN2, False)  # AIN2
    GPIO.output(AIN1, False)  # AIN1

    R_Motor.ChangeDutyCycle(0)
    GPIO.output(BIN2, False)  # BIN2
    GPIO.output(BIN1, False)  # BIN1


# 加速
def cmd_shift():
    global L_Motor
    global R_Motor
    global speed
    if speed <= 95:
        speed = speed + 5
    L_Motor.ChangeDutyCycle(speed)
    R_Motor.ChangeDutyCycle(speed)


# 减速
def cmd_ctrl():
    global L_Motor
    global R_Motor
    global speed
    if speed >= 5:
        speed = speed + 5
    L_Motor.ChangeDutyCycle(speed)
    R_Motor.ChangeDutyCycle(speed)


# 左转
def cmd_left():
    L_Motor.ChangeDutyCycle(speed)
    R_Motor.ChangeDutyCycle(speed)
    if direction_state == 1:
        GPIO.output(AIN2, True)  # AIN2
        GPIO.output(AIN1, False)  # AIN1
        GPIO.output(BIN2, False)  # BIN2
        GPIO.output(BIN1, True)  # BIN1
    else:
        GPIO.output(AIN2, True)  # AIN2
        GPIO.output(AIN1, False)  # AIN1
        GPIO.output(BIN2, False)  # BIN2
        GPIO.output(BIN1, True)  # BIN1
    time.sleep(time_stop)
    cmd_stop()


# 右转
def cmd_right():
    L_Motor.ChangeDutyCycle(speed)
    R_Motor.ChangeDutyCycle(speed)
    if direction_state == 1:
        GPIO.output(AIN2, False)  # AIN2
        GPIO.output(AIN1, True)  # AIN1
        GPIO.output(BIN2, True)  # BIN2
        GPIO.output(BIN1, False)  # BIN1
    else:
        GPIO.output(AIN2, False)  # AIN2
        GPIO.output(AIN1, True)  # AIN1
        GPIO.output(BIN2, True)  # BIN2
        GPIO.output(BIN1, False)  # BIN1
    time.sleep(time_stop)
    cmd_stop()


switch_cmd = {
    "stop": cmd_stop,
    "shift": cmd_shift,
    "ctrl": cmd_ctrl,
    "right": cmd_right,
    "left": cmd_left,
    "up": cmd_up,
    "down": cmd_down,
}


