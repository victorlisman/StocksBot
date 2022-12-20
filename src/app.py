import asyncio
import websockets
from bot import getResponse

async def handler(websocket):
    async for message in websocket:
        message = await websocket.recv()

        print(f'You: {message}')
        print(f'Bot: {getResponse(message)}')
        await websocket.send(getResponse(message))


async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())