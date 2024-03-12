import asyncio
import websockets

class Cliente():

    def __init__(self):
        pass

    async def client(self):
        url = "ws://localhost:8765"
        async with websockets.connect(url) as websocket:
            while True:
                await websocket.send("ping")
                print("enviado: ping")
                await asyncio.sleep(1)
                response = await websocket.recv()
                print(f"Recebido: {response}")

if __name__ == "__main__":
    Cliente = Cliente()
    asyncio.get_event_loop().run_until_complete(Cliente.client())    