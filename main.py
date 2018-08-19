import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=14)

# now (unix-time)
timestamp = int(time.mktime(datetime.datetime.now().timetuple()))

result = instance.read()
print("{")
print("  \"deviceName\": \"myRaspberryPi3\",")
print("  \"timeStamp\": %d," % timestamp)

if result.is_valid():
    print("  \"temperature\": %d," % result.temperature)
    print("  \"humidity\": %d" % result.humidity)
else:
    print(" \"error\": %d" % result.error_code)
print("}")
