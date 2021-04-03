#!/usr/bin/env python

# WSS (WS over TLS) server example, with a self-signed certificate

import asyncio
import websockets

async def hello(websocket, path):
#    while True:
        await websocket.send("hello world")

'''ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
cert_pem = pathlib.Path(__file__).with_name("cert.pem")
key_pem = pathlib.Path(__file__).with_name("key.pem")
ssl_context.load_cert_chain(cert_pem, key_pem)'''

start_server = websockets.serve(
    hello, "localhost", 8765
)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
