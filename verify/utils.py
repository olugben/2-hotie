 # Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACd07bfb24bd5f096999d34533fa12bff7'
auth_token = 'f4751578b8d52c6a12e3529a1cd62c9c'
client = Client(account_sid, auth_token)

def send_sms(user_code, phone_number):
    message=client.messages.create(
        body=f'Hi! your verification code is {user_code}',
        from_='+17432285936',
        to=f'{phone_number}'
    )
    print(message.sid)  
