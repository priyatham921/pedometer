import paho.mqtt.client as mqtt 
import datetime
import sys

broker_address="192.168.105.26" 


#recieve timestamp1 and publish timestamp2 in return 
def onMessage(client, userdata, msg):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    client.publish("timestamp2",now)#publish
    print("[+] Recieved time: ", msg.payload.decode())
    print("[+] Published time :", now, " published successfully")



#create new instance
client = mqtt.Client("pythonClient2") 


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

