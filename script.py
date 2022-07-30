import RPi.GPIO as GPIO
import time
 
channel = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.setup(12,GPIO.OUT,initial=GPIO.LOW)  
GPIO.setup(16,GPIO.OUT,initial=GPIO.LOW)