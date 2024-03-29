import asyncio
import websockets

class Server():

    def __init__(self) -> None:
        pass
    
    async def ping_pong(self, websocket):
        async for mensagem in websocket:
            if mensagem == "ping":
                print("Recebido: ping")
                await asyncio.sleep(1)
                await websocket.send("pong")
                print("Enviado: pong")

    async def start_server(self):
        async with websockets.serve(self.ping_pong, "localhost", 8765):
            await asyncio.Future()

if __name__ == "__main__":
    server = Server()
    asyncio.run(server.start_server())