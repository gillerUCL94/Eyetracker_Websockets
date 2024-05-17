import websocket
import asyncio
import json


url = "ws://192.168.75.51"


def on_message(ws, message): 
	print("Recived message:", message)


def on_error(ws, error):
	print("Websocket error: ", error)

def on_close(x, self, ws):
	print("WebSocket closed")



def on_open(ws): 
	print("Websocket connection established")


#	event_data = {

#	"event_type": "blink", 
#	"timestamp": "2024-05-08T12:00:00", 
#	"details": "Blink event detected"



#	}
	#ws.send(json.dumps(event_data))

websocket.enableTrace(True)

ws = websocket.WebSocketApp(url, subprotocols = ["g3api"],
							on_message = on_message, 
							on_error = on_error, 
							on_close = on_close)



ws.on_open = on_open
ws.run_forever()