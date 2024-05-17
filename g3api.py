import websocket

url = "ws://192.168.75.51/websocket"


subprotocol = "g3api"

ws = websocket.create_connection(url, subprotocols=[subprotocol])


k