import websocket
import asyncio
import json
import time

url = "ws://192.168.75.51/websocket"


subprotocol = "g3api"

class EyeTrackerWebSocketApp(websocket.WebSocketApp):

	def on_message(self, message): 
		print("Recived message:", message)


	def on_error(self, error):
		print("Websocket error: ", error)

	def on_close(self, ws):
		print("WebSocket closed")



	def on_open(self): 
		print("Websocket connection established")



websocket.enableTrace(True)
event_data = {

			"path": "recorder!start", "id": 17, "method": "POST", "body": []

			}	

ws = EyeTrackerWebSocketApp(url, subprotocols = ["g3api"])
ws.send(json.dumps(event_data))
#'ws.on_open = on_open
#print(ws_recv())
result = ws.recv()

print(result)
ws.run_forever()
#ws.close()
