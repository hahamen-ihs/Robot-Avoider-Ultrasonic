import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
# definisi motor robot
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
#definisi sensor ultrasonic
trigger_pin = 3
echo_pin = 2


GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

def send_trigger_pulse():
    GPIO.output(trigger_pin, True)
    time.sleep(0.0001)
    GPIO.output(trigger_pin, False)

def wait_for_echo(value, timeout):
    count = timeout
    while GPIO.input(echo_pin) != value and count > 0:
        count = count - 1

def get_distance():
    send_trigger_pulse()
    wait_for_echo(True, 10000)
    start = time.time()
    wait_for_echo(False, 10000)
    finish = time.time()
    pulse_len = finish - start
    distance_cm = pulse_len / 0.000058
    return (distance_cm)
    
try:
    while True:
        print("cm=%f" % get_distance())
        if get_distance()<30.00:
            print("belok" )
            GPIO.output(14, 0)
            GPIO.output(15, 1)
            GPIO.output(23, 1)
            GPIO.output(24, 0)
        else:
            print("lurus" )
            GPIO.output(14, 0)
            GPIO.output(15, 1)
            GPIO.output(23, 0)
            GPIO.output(24, 1)
        
finally:
    print("Beres")
    GPIO.cleanup()       



    
