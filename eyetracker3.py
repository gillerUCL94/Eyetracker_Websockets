from websocket import create_connection
import requests 
import json
import time

#wsapp = websocket.WebSocketApp("ws://192.168.75.51/websocket" , subprotocols = ["g3api"], on_message = on_message)
#wsapp.run_forever()


ws = create_connection("ws://192.168.75.51/websocket", subprotocols = ["g3api"])
#ws.send(json.dumps({"path": "system.recording-unit-serial", "id":22, "method": "GET"}))
ws.send(json.dumps({"path": "recorder!start", "id": 17, "method": "POST", "body": [] }))
result = ws.recv()
print (result)
time.sleep(20)
ws.send(json.dumps({"path": "recorder!stop", "id": 17, "method": "POST", "body": [] }))
result = ws.recv()
print (result)
ws.close