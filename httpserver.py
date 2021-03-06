import http.server
import socketserver

# socket handler
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self): # handles GET request. Serves the index.html page
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 9001
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()
