import asyncio

from src.server import AsyncWebSocketServer


HOST = "localhost"
PORT = 8000


async def main():
    server = AsyncWebSocketServer()
    await server.connect(HOST, PORT)


if __name__ == "__main__":
    asyncio.run(main())
