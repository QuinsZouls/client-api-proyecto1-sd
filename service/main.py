import asyncio
import json
import logging
import websockets
import os
import threading
# Env
SERVER_PORT = os.getenv('SERVER_PORT', 6789)
SERVER_URL = os.getenv('SERVER_URL', "localhost")

# Setup logging
logging.basicConfig()

# Body response

CONNECTED_RESPONSE = {
    "status": "ok",
    "type": "info",
    "response": "Connection established"
}


async def handleEncryptImage(ws, image):
  await ws.send(json.dumps({
    "status": "ok",
    "type": "result_image",
    "image": image
  }))

async def init_connection(websocket, path):
    try:
        await websocket.send(json.dumps(CONNECTED_RESPONSE))
        async for message in websocket:
            data = json.loads(message)
            if data['option'] == 'uploadImage':
                _thread = threading.Thread(target=asyncio.run, args=(handleEncryptImage(websocket, data['image'] ),))
                _thread.start()

    except:
        print("Error starting server")

# Start server
start_server = websockets.serve(init_connection, SERVER_URL, SERVER_PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()