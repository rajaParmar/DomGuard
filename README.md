# DOMGuard

DOMGuard is a integrity checker for web pages. It is based on [DOMtegrity](https://github.com/toreini/DOMtegrity).

## Features

- Stops event propagation
- Observes webpage mutations
- Uses websockets for secure communication
- Uses HMAC SHA-256 for generating signatures
- Accepts or rejects requests based on signature on the server
- Has very low overheads for webpage processing and server processing

## Installation and running

DOMGuard requires Python 3 to run. It requires http.server, socketserver and simple_websocket_server.

To use DOMGuard, copy the `<script>` tag from index.html to the required webpage at the start of the HTML file inside `<head>`. Add `document.pid.request()` to your submit button.

Install the dependencies and start the HTTP server by typing into a terminal

```sh
cd into the source folder
python3 httpserver.py
By default, HTTP server runs on localhost:9001/
```

In another terminal, start WebSocket Server

```sh
cd into the source folder
python3 websocketserver.py
By default, HTTP server runs on localhost:9000/
```

## License
**Free Software, Hell Yeah!**
