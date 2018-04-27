# ESP32 Microcontroller Sensor code
This contains the code to enable sensor readings utilising an ESP32 microcontroller

**This is a work in progress**

## Getting Started
Clone this repo to a location from which you can upload to your ESP32 microcontroller running MicroPython

```
git clone https://github.com/mqvivarium/EP32.git
```

### Config
Copy `config/config.py.example` to `config/config.py`, then adjust the config values

```
# Set the SSID for your WiFi network
SSID = 'YourSSID'

# Set the password for your WiFi network
WIFI_PASSWORD = 'YourWIFIPassword'

# Time in seconds to wait between registering on the network
# and attempting the sensor readings
NETWORK_WAIT = 20

# IP address of your MQTT broker
MQTT_BROKER = '127.0.0.1'

# Client name you want to publish to your broker as
CLIENT_ID = 'ClientName'

# Name to give the temperature reading topic
TOPIC_TEMP = 'NameOfTemperatureTopic'

# Name to give the humidity reading topic
TOPIC_HUMID = 'NameOfHumidityTopic'

# Time in seconds between each attempt reading the DHT22, MUST be greater than 2
SENSOR_SLEEP = 30

# Data in pin number
DHT22_PIN = 15
```

### Copy files to your board
Copy `main.py`, `config/` and `mq/` to the root of your board

You should then have a structure like

```
/home/pi/projects/ESP32> ls -la /pyboard/
    75 Jan  1 2000  boot.py
     0 Jan  1 2000  config/
   249 Jan  1 2000  main.py
     0 Jan  1 2000  mq/
```

### Dependencies
You will need a copy of the micropython-lib umqtt.simple file

[simple.py](https://github.com/micropython/micropython-lib/tree/master/umqtt.simple/umqtt)

Make a directory `umqtt` in root of your board and copy simple.py to that directory.

```
/home/pi/projects/ESP32> mkdir /pyboard/umqtt
/home/pi/projects/ESP32> cp simple.py /pyboard/uqmtt/
```
## Running the code
When the ESP32 microcontroller boots it will automatically run the `main.py` file.
So just rebooting the board is sufficient to connect to your WiFi network and begin reading the sensor data.

Sensor data will be published to your MQTT broker at the interval your specified in the configuration file.
