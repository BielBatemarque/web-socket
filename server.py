import asyncio
import websockets
import threading

class Server():
    
    def __init__(self):
        pass

    async def ping_pong(self, websocket, path):
        async for mensagem in websocket:
            if mensagem == "ping":
                print("Recebido: ping")
                await asyncio.sleep(1)
                await websocket.send("pong")
                print("Enviado: pong")

    def start_server(self):
        # Cria um novo loop de eventos para o thread
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        # Inicia o servidor dentro do loop de eventos
        start_server = websockets.serve(self.ping_pong, "localhost", 8765)
        loop.run_until_complete(start_server)
        loop.run_forever()

if __name__ == "__main__":
    server = Server()
    server_thread = threading.Thread(target=server.start_server)
    server_thread.start()