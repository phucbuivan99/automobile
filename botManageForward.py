import requests
from datetime import datetime, timedelta, time
import operator
import json
import collections
import mysql.connector
from botHandler import *
import mysql.connector
from telethon import functions, types, events
from telethon.tl.types import ChatInvite
from telethon.sync import TelegramClient, events, types
from telethon.tl.types import ChatInviteAlready,Chat, ChannelForbidden, ChannelParticipantsAdmins
from telethon.tl.functions.channels import JoinChannelRequest
import time
import asyncio
import unidecode
import re


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

#format string thành viết liền, không dấu, bỏ icon, bỏ kí tự đặc biệt
def formatName(text):
    text = unidecode.unidecode(text)
    text = re.sub(r'[^(a-z|A-Z|0-9)]', '', text)
    re.sub(r'[^\w]', '', text)
    return text


#tìm những tên sau kí tự @
listName=[]
def detectName(str):
    for word in str.split():
        if word.startswith('@') and len(word) >= 3:
            listName.append(word[1:])
    return listName


# get data from database
phone_number =''
api_id = 0
api_hash = ''
id_group = 0
def getData(user_id):
    sql = "SELECT * FROM customer WHERE user_id = {}".format(user_id)
    mycursor.execute(sql)
    res= mycursor.fetchone()
    global phone_number, api_id, api_hash, id_group
    phone_number = str(res['phone_number'])
    api_id = int(res['api_id'])
    api_hash = res['api_hash']
    id_group = int(res['id_group'])


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
                    first_chat_id = current_update['channel_post']['chat']['id']
                    first_chat_text = current_update['channel_post']['text']
                    user_id = current_update['channel_post']['sender_chat']['id']
                    group_title = current_update['channel_post']['chat']['title']
                    
                    if first_chat_text:
                        my_bot.send_message(first_chat_id," ")
                        new_offset = first_update_id + 1
            
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
                    getData(user_id)
                    # print(phone_number, id_group)
                    if first_chat_id == id_group:
                    # id cua group quan ly cac acc clone
                        client = TelegramClient(phone_number, api_id, api_hash)
                        client.start()
                        print(detectName(first_chat_text))

                        #kiểm tra danh sách người nhận cụ thể
                        #nếu danh sách rỗng thì gửi đến toàn bộ dialog, ngoại trừ group trung gian
                        if len(detectName(first_chat_text)) == 0:
                            for dialog in client.iter_dialogs():
                                if dialog.id != id_group and dialog.id < 0:
                                    print('{} has id {}'.format(dialog.name, dialog.id))
                                    print(message_id)
                                    try:
                                        # send_message chỉ gửi được tin nhắn text
                                        # nếu muốn gửi tin nhắn có icon các kiểu con đà điểu thì phải dùng forward
                                        # client.send_message(dialog.id, first_chat_text)
                                        client.forward_messages(dialog.id,,id_group)
                                    except:
                                        print('{} - khong gui duoc vao group nay'.format(dialog.name))
                        #gửi đến những tên được nhắc sau @
                        # else:
                        #     for dialog in client.iter_dialogs():
                        #         dialogName = formatName(dialog.name)
                        #         for i in listName:
                        #             if i == dialogName:
                        #                 # try:
                        #                 client.forward_messages(dialog.id,message_id, id_group)
                        #                 # except:
                        #                 #     print('{} - khong gui duoc vao group nay'.format(dialog.name))
                        #                 break
                                    
                        listName.clear()
                        client.disconnect()

                    
  

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()