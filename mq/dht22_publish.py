from time import sleep
from dht import DHT22
from machine import Pin
import mq.vivlib as viv
import config.config as cnf

def startSensing():
    sensor = DHT22(Pin(cnf.DHT22_PIN, Pin.IN, Pin.PULL_UP))
    ledPublish = None if cnf.LED_PUBLISH_PIN == None else Pin(cnf.LED_PUBLISH_PIN, Pin.OUT)
    ledRead = None if cnf.LED_READ_PIN == None else Pin(cnf.LED_READ_PIN, Pin.OUT)
    client = viv.initMQTTClient(cnf.MQTT_BROKER, cnf.CLIENT_ID)

    try:
        while True:
            try:
                if isinstance(ledRead, Pin): ledRead.value(1)
                    
                readings = viv.readValues(sensor)
                print(readings)
                t,h = readings
                
                if isinstance(ledRead, Pin): ledRead.value(0)
                if isinstance(ledPublish, Pin): ledPublish.value(1)
                    
                viv.publishValue(client, cnf.TOPIC_TEMP, t)
                viv.publishValue(client, cnf.TOPIC_HUMID, h)
                
                if isinstance(ledPublish, Pin): ledPublish.value(0)
            except OSError:
                print('Failed to read sensor')
            sleep(cnf.SENSOR_SLEEP)
    except KeyboardInterrupt:
        print("\nCtrl-C pressed. Cleaning up and exiting")
    finally:
        client.disconnect()
        if isinstance(ledPublish, Pin): ledPublish.value(0)
        if isinstance(ledRead, Pin): ledRead.value(0)

