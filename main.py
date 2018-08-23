import RPi.GPIO as GPIO
import dht11
import time
import datetime
from time import sleep

CONNECTION_RETRY = 5

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

def recode_dht11_data():
    # read data using pin 14
    instance = dht11.DHT11(pin=14)

    # now (unix-time)
    now = datetime.datetime.now()
    month = now.strftime("%Y%m")
    timestamp = int(time.mktime(now.timetuple()))

    result = instance.read()

    if result.is_valid():
        print("{")
        print("  \"deviceName\": \"myRaspberryPi3_%s\"," % month)
        print("  \"timeStamp\": %d," % timestamp)
        print("  \"temperature\": %d," % result.temperature)
        print("  \"humidity\": %d" % result.humidity)
        print("}")
        return True
    else:
        return False

def recode_retry_over_error():
    now = datetime.datetime.now()
    month = now.strftime("%Y%m")
    timestamp = int(time.mktime(now.timetuple()))

    print("{")
    print("  \"deviceName\": \"myRaspberryPi3_%s\"," % month)
    print("  \"timeStamp\": %d," % timestamp)
    print("  \"error\": true")
    print("}")

def task_with_retry():
    for i in range(1, CONNECTION_RETRY + 1):
        result = recode_dht11_data()
        if result == True:
            return True
    return False

result = task_with_retry()
if result != True:
    recode_retry_over_error()
