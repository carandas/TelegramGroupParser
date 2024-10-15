import asyncio
import configparser
import json

from telethon.sync import TelegramClient
from telethon import connection

from datetime import date, datetime

from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

from telethon.tl.functions.messages import GetHistoryRequest

from telethon import events

import time

config = configparser.ConfigParser()
config.read("config.ini")

api_id: str = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
user_config = config['Telegram']['username']

client = TelegramClient(user_config, api_id, api_hash, system_version="4.16.30-vxCUSTOM")

client.start()

a = input("Введите cсылку на чат: ")

async def main():
   async with client as s:
        chat_entity = await s.get_entity(a)
        async for message in s.iter_messages(chat_entity):
           await handler(message)



async def handler(event):
    sender = await event.get_input_sender()
    user = await client.get_entity(sender)
    print(user.phone)
    print("___________")
    time.sleep(0.5)

with client:
    client.loop.run_until_complete(main())


# async def dump_all_participants(channel):
#     offset_user = 0
#     limit_user = 5
#
#     all_participants = []
#     filter_user = ChannelParticipantsSearch('')
#
#     while True:
#         participants = await client(GetParticipantsRequest(channel, filter_user, offset_user, limit_user, hash=0))
#
#         if not participants.users:
#             print(participants)
#             break
#
#
#         all_participants.extend(participants.users)
#         offset_user += len(participants.users)
#
#
#
# async def Main():
#     #about_me = await client.get_entity('me')
#     #print(about_me.phone)
#
#     url = input("Введите ссылку на канал или чат: ")
#     channel = await client.get_entity(url)
#     await dump_all_participants(channel)
#
#
#
# with client:
#     try:
#         client.loop.run_until_complete(Main())
#         print("AAA")
#     finally:
#         client.disconnect()
#         print("SS")









