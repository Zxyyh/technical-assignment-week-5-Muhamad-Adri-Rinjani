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
 
# infinite loop
while True:
        time.sleep(1)