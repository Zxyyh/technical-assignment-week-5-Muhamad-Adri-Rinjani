# technical-assignment-week-5-Muhamad-Adri-Rinjani

Fritzing :
![Screenshot 2022-07-30 231133](https://user-images.githubusercontent.com/91713155/181925760-b11ed8ec-a885-40e1-94a6-087ce0fe7921.jpg)

## sensor.py :

import RPi.GPIO as GPIO
import time

channel = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.setup(12,GPIO.OUT,initial=GPIO.LOW)  
GPIO.setup(16,GPIO.OUT,initial=GPIO.LOW)
 
## main.py :
import RPi.GPIO as GPIO
import time

channel = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
GPIO.setup(12,GPIO.OUT,initial=GPIO.LOW)  
GPIO.setup(16,GPIO.OUT,initial=GPIO.LOW)
 
def callback(channel):
        if GPIO.input(channel):
                print "Air Terdeteksi!"
		    GPIO.output(12,GPIO.HIGH)
		    GPIO.output(16,GPIO.LOW)
        else:
                print "Air Tidak Terdeteksi!"
 		    GPIO.output(16,GPIO.HIGH)
		    GPIO.output(12,GPIO.LOW)
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # Pemberitahuan saat pin menjadi TINGGI atau RENDAH
GPIO.add_event_callback(channel, callback)  # Tetapkan fungsi ke PIN GPIO, Jalankan fungsi saat berubah
 
#infinite loop
while True:
        time.sleep(1)
