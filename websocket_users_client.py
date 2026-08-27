import websockets
import asyncio

async def msg():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as connect:
        message = "Привет сервер"
        print (f'Отправка: {message}')
        await connect.send(message)
        for x in range(5):
            response = await connect.recv()
            print(f'Получено сообщение от сервера: {response}')

asyncio.run(msg())