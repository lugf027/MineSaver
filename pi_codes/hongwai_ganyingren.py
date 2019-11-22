
import RPi.GPIO as GPIO
import time


hongwai_ganyingren = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(hongwai_ganyingren, GPIO.IN)


try:
	f_rec = open("hongwai_jilu.txt", "w") 
	tmp = ""
	while True:
		if GPIO.input(hongwai_ganyingren) == True:
			date_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + "with somebody Here!"
			if date_str != tmp:
				print(date_str)
				f_rec.writelines(date_str+"\n")
				tmp = date_str
		else:
			date_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())) + "with nobody!"
			if date_str != tmp:
				print(date_str)
				f_rec.writelines(date_str+"\n")
				tmp = date_str
except KeyboardInterrupt:
	f_rec.close()
	hongwai_ganyingren.stop()
	GPIO.cleanup
	
f_rec.close()
hongwai_ganyingren.stop()
GPIO.cleanup
