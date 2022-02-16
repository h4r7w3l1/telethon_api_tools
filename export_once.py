#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: h4r7w3l1 https://github.com/h4r7w3l1

import argparse
import pandas as pd
from telethon import TelegramClient, sync
import configparser

config = configparser.ConfigParser()
config.read(config_ini)

api_id = config['App']['api_id']
api_hash = config['App']['api_hash']

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--channel', action='store', dest='channel', required=True, type=str)
args = parser.parse_args()

data = []

client = TelegramClient('session_name', api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    print('Need ')
    phonenumber = input('phone:')
    client.send_code_request(phonenumber)
    client.sign_in(phonenumber, input('Enter the code: '))

for message in client.get_messages(args.channel, limit=None):
    data.append(message.text)
    print(message.text) #debug print

df = pd.DataFrame(data, columns='MESSAGE') # creates a new dataframe
df.to_csv(args.channel+'.csv', encoding='utf-8') # save to a CSV file
