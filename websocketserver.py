from simple_websocket_server import WebSocketServer, WebSocket
from secrets import token_bytes
import hmac, hashlib, re

sessionData = {}

def getsha256hmac(key, message):
    return hmac.new(key, message, hashlib.sha256).hexdigest()
    
def clean(string):
    return re.sub("[\'\"\\n\\r\\s]","",string)

def generatePID(filename):
    with open(filename) as file:
        line = file.read()
    mutation = '2222222222222222211'
    pid = mutation + clean(line)
    return pid

def make_decision(h1 ,h2, sessionID):
	decision_vector = []
	reason = ""
	decision = ""
	if(h1 == h2):
		if(sessionData[sessionID]["decision"] == False):
			sessionData[sessionID]["decision"] = True
			decision = "Accept"
			reason = "Signatures match!"
		else:
			decision = "Reject"
			reason = "There was another request from your browser"
	else:
		decision = "Reject"
		reason = "Signatures don't match!"

	decision_vector.append(decision)
	decision_vector.append(reason)
	return decision_vector

class DomGuard(WebSocket):
    def handle(self):
        sessionID = self.request.headers._headers[10][1]
        pid = bytes(generatePID('index.html'), 'utf-8')
        temp = getsha256hmac(sessionData[sessionID]["private"], pid)
       	print(make_decision(temp, self.data.hex(), sessionID))

    def connected(self):
        sessionID = self.request.headers._headers[10][1]
        sessionData[sessionID] = {"private" : token_bytes(32), "decision" : False}
        self.send_message(sessionData[sessionID]["private"].hex())
        print(self.address, 'connected')

    def handle_close(self):
        sessionID = self.request.headers._headers[10][1]
        del sessionData[sessionID]
        print(self.address, 'closed')

server = WebSocketServer('', 9000, DomGuard)
server.serve_forever()

