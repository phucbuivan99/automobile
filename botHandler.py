import requests
import operator
import json

class botHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
        

    
    #functions get_updates
    def get_updates(self, offset=0, timeout=30):
        method_url = r'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method_url, params)
        data = json.loads(resp.text)
        if data['ok'] == True:
            result_json = data['result']
            return  result_json
        return data

    
    #function send messages    
    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method_url = r'sendMessage'
        resp = requests.post(self.api_url + method_url, params)
        return resp
    
    # #function delete message
    # def del_message(self, chat_id, message_id):
    #     params = {'chat_id':chat_id ,'message_id': message_id}
    #     method_url = r'deleteMessage'
    #     resp= requests.get(self.api_url + method_url,params)
    #     return True

    # #fucntion forward message
    # def forward_message(self, chat_id, from_chat_id, message_id):
    #     params= {'chat_id':chat_id, 'from_chat_id':from_chat_id,'message_id': message_id}
    #     method_url=r'forwardMessage'
    #     resp= requests.post(self.api_url + method_url, params)
    #     return resp

    # #function kick member
    # def kick_member(self, chat_id, user_id):
    #     params= {'chat_id': chat_id, 'user_id': user_id}
    #     method_url = r'kickChatMember'
    #     resp= requests.post(self.api_url + method_url, params)
    #     return resp

    # #check admin
    # def isAdmin(self, chat_id,user_id):
    #     params= {'chat_id': chat_id, 'user_id': user_id}
    #     method_url = r'getChatMember'
    #     resp= requests.post(self.api_url + method_url, params)
    #     data = json.loads(resp.text)
    #     print(data)
    #     if data['ok'] == True:
    #         status_member = data['result']['status']
    #     if status_member == 'admin' or status_member == 'creator':
    #         return True
    #     else:
    #         return False
    

token = '1623181614:AAE0U7Y5BoVjgP3qCA5-tHSYd7bjerpr2Mo' #Token of your bot 
# username: @Manage_Forward_Bot
#name: Manage Forward

my_bot = botHandler(token=token)