import _thread

import RPi.GPIO as GPIO
import time
from ops.ras import *
import requests
from flask import Flask, request
app = Flask(__name__)

start()


@app.route('/analyse', methods=['POST'])
def conversion():
    time = request.form.get("time")
    picture_url = request.form.get("picture_url")
    try:
        _thread.start_new_thread(con_fun, (time, picture_url))
    except:
        print("Error: 无法启动线程")
    return "start converse..."


def con_fun(cmd_op):
    try:
        cmd_func = switch_cmd.get(cmd_op)
        if cmd_func:
            cmd_func()
        else:
            print("Illegal control method")
            GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()

    GPIO.cleanup()
