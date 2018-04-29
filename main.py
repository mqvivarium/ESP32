import sys
import network
import mq.dht22_publish as mqdht
import mq.utilities as util
from time import sleep
from machine import Pin
import config.config as cnf

ledError = None if cnf.LED_ERROR_PIN == None else Pin(cnf.LED_ERROR_PIN, Pin.OUT)
ledPublish = None if cnf.LED_PUBLISH_PIN == None else Pin(cnf.LED_PUBLISH_PIN, Pin.OUT)
ledRead = None if cnf.LED_READ_PIN == None else Pin(cnf.LED_READ_PIN, Pin.OUT)

util.blink(ledError, 1, 2, 0, 0.5, 0.5)

station = network.WLAN(network.STA_IF)

for i in range(0, 2):
  util.blink(ledError, 1, 2, 0.1, 0.1, 0.1)
  util.blink(ledPublish, 1, 2, 0.1, 0.1, 0.1)
  util.blink(ledRead, 1, 2, 0.1, 0.1, 0.1)

count = 1
connect = True

if not station.isconnected():
  print('Connecting to the network...')
  station.active(True)
  station.connect(cnf.SSID,cnf.WIFI_PASSWORD)
  while not station.isconnected() and connect:
    sleep(5)
    if count > 5: 
      station.disconnect()
      print('Could not connect to the network')
      connect = False
    count += 1
  if not station.isconnected(): 
    util.blink(ledError, 5, 3, 1, 0.1, 0.1)
    sys.exit()

sleep(cnf.NETWORK_WAIT)
mqdht.startSensing()
