import RPi.GPIO as GPIO
import time

p_duoji_zhuandong = None

def start_duiji_shexiangtou():
	global p_duoji_zhuandong
	duoji_shexiangtou = 23
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(duoji_shexiangtou, GPIO.OUT)

	p_duoji_zhuandong = GPIO.PWM(duoji_shexiangtou, 50)
	p_duoji_zhuandong.start(to_num(90))


def to_num(num):
	fm = 10.0 / 180.0
	num = num * fm + 2.5
	num = int(num * 10) / 10.0
	return num


def change_cycle(num):
	try:
		if num < 0 or num > 180:
			p_duoji_zhuandong.stop()
		else:
			p_duoji_zhuandong.ChangeDutyCycle(to_num(num))
	except Exception as ex:
		p_duoji_zhuandong.stop()
		GPIO.cleanup


def end_change_cycle():
	p_duoji_zhuandong.stop()
	GPIO.cleanup

