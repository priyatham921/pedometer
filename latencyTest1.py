import paho.mqtt.client as mqtt 
import time
import datetime
import sys

broker_address="192.168.105.26" 


#recieve timestamp1 and publish timestamp2 in return 
def onMessage(client, userdata, msg):
    print("[+] Recieved time: ", msg.payload.decode())
    print("[+] timestamp2: ", time.time())



#create new instance
client = mqtt.Client("pythonClient1") 


#connect to broker
if client.connect(broker_address) == 0:
    print("[+] connected to broker") 
else:
    print("[-] Could not connec to MQTT Broker!")
    sys.exit(-1)

#publish timestamp1
ts = datetime.datetime.now().strftime("%H:%M:%S")
client.publish("timestamp1", ts)
print("[+] Published time: ", ts)
print("[+] timestamp1: ", time.time())


#subscribe to topic - timestamp2 to recieve timestamp in return
client.subscribe("timestamp2")
client.on_message = onMessage
client.loop_forever()





