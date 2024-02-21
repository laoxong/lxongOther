import asyncio
import json
import os
from io import BytesIO
import re

import httpx
import imagehash
import websockets
from PIL import Image
from dotenv import load_dotenv


class FuckSPAM:
    def __init__(self):
        self.spamImgDict = ['938db8e0adb3c616', 'ac3491c9d1cc52fb']
        self.spamWord = ["https://ctkpaarr.org/", "https://荒らし.com/"]
        self.InstanceHost = os.getenv("InstanceHost")
        self.misskeyI = os.getenv('misskeyI')
        self.s = httpx.AsyncClient(base_url=f'https://{os.getenv("InstanceHost")}')

    async def __fetch_img(self, url):
        r = await self.s.get(url)  # 理论上其他域名已经覆盖了 base_url
        return r.read(), r.status_code

    async def __suspend_user(self, __id) -> None:
        await self.s.post(f"/api/admin/suspend-user", json={"i": self.misskeyI, "userId": __id})

    async def __del_note(self, __id) -> None:
        await self.s.post(f"/api/notes/delete", json={"i": self.misskeyI, "noteId": __id})

    async def __report(self, __id) -> None:
        await self.s.post(f"/api/users/report-abuse", json={"i": self.misskeyI, "userId": __id, "comment": "疑似滥用"})

    async def __handle_message(self, message: str) -> None:
        print(message)
        mes = json.loads(message)
        try:
            if "mentions" in mes["body"]["body"] and "files" in mes["body"]["body"]:
                if len(mes["body"]["body"]["mentions"]) > 2 and len(mes["body"]["body"]["files"]) > 0:
                    file_content, _ = await self.__fetch_img(mes["body"]["body"]["files"][0]["url"])
                    memory_file = BytesIO(file_content)
                    phash = imagehash.phash(Image.open(memory_file))

                    if str(phash) in self.spamImgDict:
                        await self.__del_note(mes["body"]["body"]["id"])
                        await self.__suspend_user(mes["body"]["body"]["user"]["id"])
                        await self.__report(mes["body"]["body"]["user"]["id"])
            
            #判断网址
            url_pattern = re.compile(r'https?://\S+')
            urls = url_pattern.findall(str(mes["body"]["body"]["text"]))
            for url in urls:
                if url in self.spamWord:
                    await self.__del_note(mes["body"]["body"]["id"])
                    await self.__suspend_user(mes["body"]["body"]["user"]["id"])
                    await self.__report(mes["body"]["body"]["user"]["id"])

        except KeyError:
            ...

    async def wss_client_start(self):
        url = f"wss://{self.InstanceHost}/streaming?i={self.misskeyI}"
        try:
            async with websockets.connect(url) as ws:
                print(f"Connected to {url}")
                data = {"type": "connect", "body": {"channel": "main", "id": "1"}}
                await ws.send(json.dumps(data, ensure_ascii=False, separators=(',', ':')))
                data = {"type": "connect", "body": {"channel": "globalTimeline", "id": "2",
                                                    "params": {"withRenotes": True, "withReplies": True}}}
                await ws.send(json.dumps(data, ensure_ascii=False, separators=(',', ':')))

                async for message in ws:
                    await self.__handle_message(message)
        except websockets.exceptions.ConnectionClosedError:
            await fuck_spam.wss_client_start()


async def main():
    load_dotenv()
    fuck_spam = FuckSPAM()
    await fuck_spam.wss_client_start()


if __name__ == "__main__":
    asyncio.run(main())
