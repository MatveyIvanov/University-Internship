import asyncio
import websockets
import json


class AsyncWebSocketServer:
    def __init__(self):
        self.connected = set()
        self.handler_map = {"auth": self.auth, "message": self.message}

    async def connect(self, path: str, port: int):
        async with websockets.serve(self.handler, path, port):
            await asyncio.Future()

    async def auth(self, websocket, data: dict):
        self.connected.add(websocket)

        await websocket.send(
            json.dumps(
                {
                    "event": "auth",
                    "data": {
                        "message": f"Successfully authenticated as {data.get('username')}"
                    },
                }
            )
        )

    async def message(self, websocket, data: dict):
        websockets.broadcast(
            self.connected,
            json.dumps(
                {
                    "event": "message",
                    "data": {
                        "username": data.get("username"),
                        "message": data.get("message"),
                    },
                }
            ),
        )

    async def handler(self, websocket):
        while True:
            data = json.loads(await websocket.recv())

            await self.handler_map[data["event"]](websocket, data.get("data"))
