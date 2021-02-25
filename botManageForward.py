import requests
from datetime import datetime, timedelta, time
import operator
import json
import collections
import mysql.connector
import botHandler
import mysql.connector
from telethon import functions, types, events
from telethon.tl.types import ChatInvite
from telethon.sync import TelegramClient, events, types
from telethon.tl.types import ChatInviteAlready,Chat, ChannelForbidden, ChannelParticipantsAdmins
from telethon.tl.functions.channels import JoinChannelRequest
import time
import asyncio


mydb= mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="tool_forward",
)
mycursor= mydb.cursor(dictionary=True, buffered=True)

if mycursor:
    print("connected")
else:
    print("failed connected")

def main():
    new_offset = 0
    print('hi, now launching...')
    now= datetime.now()
    now= now.strftime("%H:%M:%S")
    print(now)
    
      

    while True:
        all_updates = my_bot.get_updates(new_offset)
       
        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)

                
                
                first_update_id = int (current_update['update_id'])
                # print(type(first_update_id))
                # print(type(first_update_id))
                if 'channel_post' in current_update:
                    message_id = current_update['channel_post']['message_id']
                    first_chat_id= current_update['channel_post']['chat']['id']
                    first_chat_text= current_update['channel_post']['text']
                    user_id= current_update['channel_post']['sender_chat']['id']
                    group_title= current_update['channel_post']['chat']['title']
                    
                    if first_chat_text:
                        my_bot.send_message(first_chat_id," ")
                        new_offset = first_update_id +1
            
                else :
                    first_chat_id = current_update['message']['chat']['id']   
                    message_id = current_update['message']['message_id']
                    user_id = current_update['message']['from']['id']
                    group_title= current_update['message']['chat']['title']
                    
                
                    
                    if 'text' not in current_update['message'] :
                        first_chat_text = 'New member'
                    else:                    
                        first_chat_text = current_update['message']['text']
                    
                    if 'last_name' in current_update['message']:   
                        first_last_name= current_update['message']['chat']['last_name']
                        
                                                    
                    elif 'first_name'  in current_update['message']:
                        first_chat_name = current_update['message']['chat']['first_name']
                    
                    elif 'message' in current_update['message']:
                        message_id = current_update['message']['message_id']
                                    
                    elif 'new_chat_member' in current_update['message']:
                        first_chat_name = current_update['message']['new_chat_member']['first_name']
                        first_last_name = " "
                        user_fullname = first_chat_name
                        
                    elif 'from' in current_update['message']:
                        first_chat_name = current_update['message']['from']['first_name']
                        if 'last_name' not in current_update['message']['from']:
                            first_last_name = " "
                        else:
                            first_last_name = current_update['message']['from']['last_name']
                        
                    elif 'left_chat_member' in current_update['message']:
                        
                        first_chat_name= current_update['message']['left_chat_member']['first_name']
                        first_last_name= " "
                        user_fullname = first_chat_name
                        
                    user_fullname= first_chat_name +" " + first_last_name

                    if first_chat_text:
                        my_bot.send_message(first_chat_id," ")
                        new_offset = first_update_id +1
                    
                    print(user_id)
                    if first_chat_id == -1001456856708:
                    # id cua group quan ly cac acc clone
                        sql = "SELECT * FROM customer WHERE user_id = {}".format(user_id)
                        mycursor.execute(sql)
                        res= mycursor.fetchone()
                        phone_number = res['phone_number']
                        api_id = int(res['api_id'])
                        api_hash = res['api_hash']
                        client = TelegramClient(phone_number, api_id, api_hash)
                        client.start()
                        for dialog in client.iter_dialogs():
                            if dialog.id != -1001456856708:
                            # id cua group quan ly cac acc clone
                                print('{} has id {}'.format(dialog.name, dialog.id))
                                try:
                                    # send_message chỉ gửi được tin nhắn text, tin nhắn có icon thì không gửi được
                                    # nếu muốn gửi tin nhắn có icon các kiểu con đà điểu thì phải dùng forward
                                    # client.send_message(dialog.id, first_chat_text)
                                    client.forward_messages(dialog.id,message_id, -1001456856708)
                                except:
                                    print('{} - khong gui duoc vao group nay'.format(dialog.name))
                        client.disconnect()

                    
  

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
        