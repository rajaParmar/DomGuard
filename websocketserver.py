from simple_websocket_server import WebSocketServer, WebSocket
from secrets import token_bytes
import hmac, hashlib, re

sessionData = {}

# Calculate the hmac of the given message using the key
def getsha256hmac(key, message):
    return hmac.new(key, message, hashlib.sha256).hexdigest()
    
# Removes spaces, newlines and quotation marks from the given string
def clean(string):
    return re.sub("[\'\"\\n\\r\\s]","",string)

# Generates page ID (PID) of the given HTML file. Mutation is hard coded for our index.html file.
# It can be changed for the required file. It can be found by using console.log in the requirede file.
def generatePID(filename):
    with open(filename) as file:
        line = file.read()
    mutation = '2222222222222222211'
    pid = mutation + clean(line)
    return pid

# Accept or reject based on matching HMAC signature and duplicate requests
def make_decision(h1 ,h2, sessionID):
	decision_vector = []
	reason = ""
	decision = ""
	if(h1 == h2): #matched signature
		if(sessionData[sessionID]["decision"] == False):
			sessionData[sessionID]["decision"] = True
			decision = "Accept"
			reason = "Signatures match!"
		else: # decision will be true if request already processed
			decision = "Reject"
			reason = "There was another request from your browser"
	else: # signature not matched
		decision = "Reject"
		reason = "Signatures don't match!"

	decision_vector.append(decision)
	decision_vector.append(reason)
	return decision_vector

class DomGuard(WebSocket): # websocket handler
    def handle(self): # code to check for integrity and make decision. Runs when browser sends websocket message
        sessionID = self.request.headers._headers[10][1]
        pid = bytes(generatePID('index.html'), 'utf-8')
        temp = getsha256hmac(sessionData[sessionID]["private"], pid)
       	print(make_decision(temp, self.data.hex(), sessionID))

    def connected(self): # code which handes websocket connection request
        sessionID = self.request.headers._headers[10][1]
        sessionData[sessionID] = {"private" : token_bytes(32), "decision" : False}
        self.send_message(sessionData[sessionID]["private"].hex())
        print(self.address, 'connected')

    def handle_close(self): #code to close websocket connection and cleanup
        sessionID = self.request.headers._headers[10][1]
        del sessionData[sessionID]
        print(self.address, 'closed')

server = WebSocketServer('', 9000, DomGuard)
server.serve_forever()

