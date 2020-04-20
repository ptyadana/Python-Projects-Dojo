import configparser
from twilio.rest import Client

config = configparser.RawConfigParser()
config.read('twilio.properties')

account_sid = config.get('TwilioSetup', 'account_sid')
auth_token = config.get('TwilioSetup', 'auth_token')
from_number = config.get('TwilioSetup', 'from_number')
to_number = config.get('TwilioSetup', 'to_number')

client = Client(account_sid, auth_token) 

msg = 'hellooooooo...testing'

message = client.messages.create( 
                              from_=from_number,        
                              to=to_number,
                              body=msg
                          ) 

print(message.sid)