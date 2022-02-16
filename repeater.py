#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: h4r7w3l1 https://github.com/h4r7w3l1

from telethon import TelegramClient, sync, events
import os
import sys
import re
import telebot
import time
from datetime import datetime
import binascii
import inspect
import logging
import json
import configparser

def get_script_dir():
    return os.path.dirname(inspect.getabsfile(get_script_dir))


config_ini = os.path.dirname(os.path.abspath('config.ini'))
logs_path = os.path.join(get_script_dir(), 'logs')

logging.basicConfig(filename='app.log',format='%(asctime)s %(levelname)s:%(message)s',level=logging.INFO)

config = configparser.ConfigParser()
config.read(config_ini)

api_id = config['App']['api_id']
api_hash = config['App']['api_hash']

client = TelegramClient('session_name', api_id, api_hash)

bot = telebot.TeleBot(config['App']['bot_api'])

def send_message(user_mess, destid):
	bot.send_message(destid, message.text)
	

@client.on(events.NewMessage(chats=config['Resend']['watch_id']))
async def normal_handler(event):
    print(event.message)
    user_mess=event.message.to_dict()['message']
    s_user_id=event.message.to_dict()['from_id']
    user_id=int(s_user_id)
    user=d.get(user_id)
    mess_date=event.message.to_dict()['date']
    f.write(mess_date.strftime("%d-%m-%Y %H:%M")+"\n")
    f.write(user+"\n")
    f.write(user_mess+"\n\n")
    send_message(user_mess, config['Resend']['receiver_id'])
    f.flush()

client.start()

group=config['Resend']['watch_group']

participants = client.get_participants(group)
users={}

for partic in client.iter_participants(group):
    lastname=""
    if partic.last_name:
       lastname=partic.last_name
    users[partic.id]=partic.first_name+" "+lastname

f=open('messages_from_chat.txt', 'a') 

bot.polling()

client.run_until_disconnected()
f.close()
