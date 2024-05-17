from websocket import create_connection
import requests 
import json
import time

#wsapp = websocket.WebSocketApp("ws://192.168.75.51/websocket" , subprotocols = ["g3api"], on_message = on_message)
#wsapp.run_forever()


ws = create_connection("ws://192.168.75.51/websocket", subprotocols = ["g3api"])
#ws.send(json.dumps({"path": "system.recording-unit-serial", "id":22, "method": "GET"}))
ws.send(json.dumps({"path": "recorder!start", "id": 17, "method": "POST", "body": [] }))
print(ws.recv())
time.sleep(3)
#result = ws.recv()
#print (result)
#time.sleep(20)
#ws.send(json.dumps({"path": "recorder!stop", "id": 17, "method": "POST", "body": [] }))

for i in range (5):
	ws.send(json.dumps({"path": "recorder!send-event", "id": 99, "method":"POST", "body": [	"gps-location",{
		"lat": 59.2,
		"long": 18.9}]}))
	time.sleep(5)
	print(ws.recv())



ws.send(json.dumps({"path": "recorder!stop", "id": 17, "method": "POST", "body":[]
	 }))
print(ws.recv())
ws.close()
