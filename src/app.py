import asyncio
import websockets
import json
import logging
from bot import getResponse

async def handler(websocket):
    async for message in websocket:
        sentence = json.loads(message)

        print(f'You: {sentence}')
        print(f'Bot: {getResponse(message)}')
        await websocket.send(json.dumps(getResponse(message)))


async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())