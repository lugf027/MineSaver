
import RPi.GPIO as GPIO
import time

duoji_shexiangtou = 23

# duoji jiaodu de zhuannhuan
def to_num(num):
	fm = 10.0 / 180.0
	num = num * fm + 2.5
	num = int(num * 10) / 10.0
	return num

GPIO.setmode(GPIO.BCM)
GPIO.setup(duoji_shexiangtou, GPIO.OUT)

p_duoji_zhuandong = GPIO.PWM(duoji_shexiangtou, 50)
p_duoji_zhuandong.start(to_num(0))

try:
	while True:
		num = int(input("num"))
		if num < 0 or num > 180:
			p_duoji_zhuandong.stop()
		else:
			p_duoji_zhuandong.ChangeDutyCycle(to_num(num))
except KeyboardInterrupt:
	p_duoji_zhuandong.stop()
	GPIO.cleanup

p_duoji_zhuandong.stop()
GPIO.cleanup

