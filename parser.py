import asyncio
import traceback
from datetime import datetime, timedelta
import pyrogram
from data import config
from base_control import Control
controller = Control()


class TgParser:


    def __init__(self):
        self.status = False
        try:
            self.client = pyrogram.Client(phone_number=config.USER_PHONE_NUMBER, api_hash=config.USER_API_HASH,
                                          api_id=config.USER_API_ID, name="default_user")
            self.client.start()
            self.status = True
        except:
            traceback.print_exc()
            self.status = False




    async def __get_all_messages_on_chat(self, chat_id, start_time, next=False):
        try:
            messages = []
            temp = []
            await self.client.connect()
            end_time = datetime.now()
            print(start_time)
            current_date = start_time
            while current_date < end_time:
                async for msg in self.client.get_chat_history(chat_id=chat_id,limit=1000,offset=0,offset_date=current_date):
                    if msg.id not in temp:
                        defir = msg.date - start_time
                        if defir.total_seconds() >= 0:
                            messages.append(msg)
                            temp.append(msg.id)
                current_date = current_date + timedelta(days=1)
                await asyncio.sleep(3)
            return messages
        except:
            traceback.print_exc()
            return False
        finally:
            if not next:
                await self.client.disconnect()


    async def get_redy_messages_on_chat(self, chat_id, word:str, min_day=1, next=False):
        result = []
        start_time = datetime.now() - timedelta(days=min_day)  # Last 7 days
        all = await self.__get_all_messages_on_chat(chat_id, start_time, next)
        if all:
            for msg in all:
                if msg.text:
                    if word.lower() in msg.text.lower():
                        text = msg.text
                        result.append(text)
                elif msg.caption:
                    if word.lower() in msg.caption.lower():
                        text = msg.caption
                        result.append(text)

        if len(result) > 0:
            return result
        else:
            return None



    async def join_to_channels(self, channels = []):
        joined = []
        await self.client.connect()
        for channel in channels:
             await asyncio.sleep(3)
             if not controller.check_joined_channel_exists(channel):
                 try:
                     chat = await self.client.join_chat(channel)
                     joined.append(chat)
                     id = chat.id
                     controller.create_joined_channel(channel, id)
                 except:
                     traceback.print_exc()
        await self.client.disconnect()
        return joined


    async def add_new_account(self):
        pass
        



async def test():
    api = TgParser()
    urls = ["@markettwits"]



if __name__ == "__main__":
    asyncio.run(test())