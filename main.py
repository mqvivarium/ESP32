import network
import mq.dht22_publish as mqdht
from time import sleep
import config.config as cnf

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(cnf.SSID,cnf.WIFI_PASSWORD)
sleep(cnf.NETWORK_WAIT)
mqdht.startSensing()
