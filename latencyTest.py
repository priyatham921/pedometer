import paho.mqtt.client as mqtt 
import datetime
import sys

broker_address="192.168.96.26" 


#recieve timestamp1 and publish timestamp2 in return 
def onMessage(client, userdata, msg):
    print("[+] Recieved timestamp1: ", msg.payload.decode())
    now = datetime.datetime.now().strftime("%H:%M:%S")
    client.publish("timestamp2",now)#publish
    print("[+] Timestamp2 :", now, " published successfully")



#create new instance
client = mqtt.Client("pythonClient") 


#connect to broker
if client.connect(broker_address) == 0:
    print("[+] connected to broker") 
else:
    print("[-] Could not connec to MQTT Broker!")
    sys.exit(-1)


#subscribe to topic - timestamp1 to recieve timestamp from js
client.subscribe("timestamp1")
client.on_message = onMessage
client.loop_forever()

