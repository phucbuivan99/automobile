# from jinja2.utils import internal_code
from telethon.sync import TelegramClient, events, types
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.channels import JoinChannelRequest
from forward_db import *
api_id = 2358245
api_hash = '4dc2303f73b28a1c0c8ecc7a25ab8d65'
phone_number = '+84394880604'
mes =''

def checkin_group(client, group_id):
    dialog_id = []
    for dialog in client.iter_dialogs():
        dialog_id.append(dialog.id)
    print(dialog_id)
    return group_id in dialog_id

    

def join_group(client, group_type, group_link):
    if group_type == 'private':
        join = client(ImportChatInviteRequest(hash=group_link))
        print('Join to private')
    elif group_type == 'public':
        join = client(JoinChannelRequest(channel=group_link))
        print('Join to public')


client = TelegramClient('Bui Van Phuc', api_id, api_hash)

# group_id= selectGroup()['group_id']


#auto join group
link= selectLink()
for i in link:
    group_type= i['group_type']
    group_link= i['group_link']

    if group_type=='private':
        group_link= group_link[22:]
    print(group_link)
    # phần này khi cần join thì bỏ cmt để join, nếu để chạy liên tục sẽ báo lỗi
    #########
    # with client:
    #     # join_group(client, group_type, group_link)
        
       


listGroup= selectGroup()




# Client forward all groups
@client.on(events.NewMessage(outgoing=True))


async def handle_command(event):
    if '/start' in event.raw_text:
        mes =''
        async for dialog in client.iter_dialogs():
                insertJoinedgroup(str(dialog.id), dialog.name)
                delDupData()
                mes += '{} has id {}\n'.format(dialog.name, dialog.id)
        await client.send_message('me',mes)
    if '/id:' in event.raw_text:
        global medium_group
        medium_group = event.raw_text[4:]
        print(type(medium_group))
    if event.chat_id == int(medium_group):
        for i in listGroup:
            if i['group_id'] != medium_group and i['group_id'] != listGroup[0]['group_id']:
                print(i['group_id'])
                await client.forward_messages(int(i['group_id']),event.message)

client.start()
client.run_until_disconnected()