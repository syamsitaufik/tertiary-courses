import paho.mqtt.client as mqtt
import time
from sense_hat import SenseHat

sense = SenseHat()

# set up mqtt client
client = mqtt.Client("python_pub")

#set mqtt username/pw
client.username_pw_set(username="pi", password="PASS")

#set server to publish to
client.connect("broker.hivemq.com", 1883)

client.loop_start()

try:
    while True:
        #publish temp to topic
        client.publish("sense/temp", sense.get_temperature())

        #publish humidity
        client.publish("sense/humid", sense.get_humidity())
        
        #publish humidity
        client.publish("sense/press", sense.get_pressure())

        #pause for 10 seconds
        time.sleep(10)

    #deal nicely with ^C

except KeyboardInterrupt:
    print("interrupted!")
    client.loop_stop()
