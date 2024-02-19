import asyncio
import os

import aiohttp
import websockets
import json
import imagehash
from dotenv import load_dotenv
from PIL import Image

spamImgDict = ['938db8e0adb3c616', 'ac3491c9d1cc52fb']
InstanceHost = os.getenv('InstanceHost')
misskeyI = os.getenv('misskeyI')

async def fetchImg(session, url):
    async with session.get(url) as response:
        return await response.read(), response.status


async def suspendUser(session, id):
    async with session.post(f"https://{InstanceHost}/api/admin/suspend-user",
                            params={"i": misskeyI, "userId": id}) as response:
        return response.status


async def delNote(session, id):
    async with session.post(f"https://{InstanceHost}/api/notes/delete", data=json.dumps({"i": misskeyI, "noteId": id}),
                            headers={"Content-Type": "application/json"}) as response:
        return response.status


async def report(session, id):
    async with session.post(f"https://{InstanceHost}/api/users/report-abuse",
                            data=json.dumps({"i": misskeyI, "userId": id, "comment": "疑似滥用"}),
                            headers={"Content-Type": "application/json"}) as response:
        return response.status


async def handle_message(message):
    print(message)
    mes = json.loads(message)
    try:
        if "mentions" in mes["body"]["body"] and "files" in mes["body"]["body"]:
            if len(mes["body"]["body"]) > 2:
                async with aiohttp.ClientSession() as session:
                    file_content, status = await fetchImg(session, mes["body"]["body"]["files"][0]["url"])

                with open("downloaded_file.png", "wb") as f:
                    f.write(file_content)
                phash = imagehash.phash(Image.open("downloaded_file.png"))

                if str(phash) in spamImgDict:
                    async with aiohttp.ClientSession() as session:
                        await delNote(session, mes["body"]["body"]["id"])
                        await suspendUser(session, mes["body"]["body"]["user"]["id"])
                        await report(session, mes["body"]["body"]["user"]["id"])
    except KeyError:
        ...


async def main():
    url = f"wss://{InstanceHost}/streaming?i={misskeyI}"
    async with websockets.connect(url) as websocket:
        print(f"Connected to {url}")
        await websocket.send('{ "type": "connect", "body": { "channel": "main", "id": "1" } }')
        await websocket.send(
            '{"type":"connect","body":{"channel":"globalTimeline","id":"2","params":{"withRenotes":true,'
            '"withReplies":true}}}')
        while True:
            message = await websocket.recv()
            await handle_message(message)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
