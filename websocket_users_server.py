import asyncio
import websockets


from websockets import ServerConnection

async def cons(connection: ServerConnection):
    async for message in connection:
        print(f"Получено сообщение: {message}")
        for x in range(5):
            response = f'{x} Сообщение пользователя: {message}'
            await connection.send(response)


async def main():
    server = await websockets.serve(cons,"localhost",8765)
    print("Сервер запущен")
    await server.wait_closed()


asyncio.run(main())