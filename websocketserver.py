from simple_websocket_server import WebSocketServer, WebSocket
from secrets import token_bytes
import hmac, hashlib

def getsha256hmac(key, message):
    return hmac.new(key, message, hashlib.sha256).hesdigest()

sessionData = {}
class SimpleEcho(WebSocket):
    def handle(self):
        # echo message back to client   
        sessionID = self.request.headers._headers[10][1]
        print("handle "+sessionID)
        print(self.data)

    def connected(self):
        print(self.address, 'connected')
        sessionID = self.request.headers._headers[10][1]
        print("connect "+sessionID)
        sessionData[sessionID] = {"private" : token_bytes(32),"iv" : token_bytes(16), "decision" : False}
        print(sessionData[sessionID])
        self.send_message(sessionData[sessionID]["private"].hex() + " " + sessionData[sessionID]["iv"].hex())
        print("connection success")

    def handle_close(self):
        print(self.address, 'closed')

server = WebSocketServer('', 9000, SimpleEcho)
server.serve_forever()

