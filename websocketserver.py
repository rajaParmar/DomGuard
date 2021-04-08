from simple_websocket_server import WebSocketServer, WebSocket
from secrets import token_bytes
import hmac, hashlib, re

def getsha256hmac(key, message):
    return hmac.new(key, message, hashlib.sha256).hexdigest()
    
def clean(string):
    return re.sub("[\'\"\\n\\r\\s]","",string)

def generatePID(filename):
    file = open(filename)
    line = file.read()
    mutation = '2222222222222222211'
    pid = mutation + clean(line)
    return pid


def make_decision(h1,h2,sessionID):
	decision_vector = []
	reason = ""
	decision = ""
	if(h1 == h2):
		if(sessionData[sessionID]["decision"] == False):
			sessionData[sessionID]["decision"] = True
			decision = "accept"
			reason = "signatures match!"
		else:
			decision = "reject"
			reason = "There was another request from your browser"
	else:
		decision = "reject"
		reason = "signatures don't match!"

	decision_vector.append(decision)
	decision_vector.append(reason)

	return decision_vector

sessionData = {}
class DomGuard(WebSocket):
    def handle(self):
        sessionID = self.request.headers._headers[10][1]
        pid = bytes(generatePID('index.html'), 'utf-8')
        temp = getsha256hmac(sessionData[sessionID]["private"], pid)
       	print(make_decision(temp,self.data.hex(),sessionID))

    def connected(self):
        print(self.address, 'connected')
        sessionID = self.request.headers._headers[10][1]
        sessionData[sessionID] = {"private" : token_bytes(32), "decision" : False}
        self.send_message(sessionData[sessionID]["private"].hex())
        print("connection success")

    def handle_close(self):
        print(self.address, 'closed')

server = WebSocketServer('', 9000, DomGuard)
server.serve_forever()

