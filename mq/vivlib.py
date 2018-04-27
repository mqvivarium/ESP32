from umqtt.simple import MQTTClient

def initMQTTClient( server, clientId ):
    client = MQTTClient(clientId, server)
    client.connect()
    return client

def readValues( sensor ):
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    return [t,h]

def publishValue( client, topic, value ):
    if isinstance(value, float):
        msg = (b'{0:3.1f}'.format(value))
        client.publish(topic, msg)
    else:
        print('Invalid sensor reading')
