from time import sleep
from dht import DHT22
from machine import Pin
import mq.vivlib as viv
import config.config as cnf

def startSensing():
    sensor = DHT22(Pin(cnf.DHT22_PIN, Pin.IN, Pin.PULL_UP))
    client = viv.initMQTTClient(cnf.MQTT_BROKER, cnf.CLIENT_ID)

    try:
        while True:
            try:
                readings = viv.readValues(sensor)
                print(readings)
                t,h = readings
                viv.publishValue(client, cnf.TOPIC_TEMP, t)
                viv.publishValue(client, cnf.TOPIC_HUMID, h)
            except OSError:
                print('Failed to read sensor')
            sleep(cnf.SENSOR_SLEEP)
    except KeyboardInterrupt:
        print("\nCtrl-C pressed. Cleaning up and exiting")
    finally:
        client.disconnect()

