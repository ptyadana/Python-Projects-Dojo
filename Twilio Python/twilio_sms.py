from twilio.rest import Client

account_SID = 'Your Twilio Account SID'
auth_token = 'Your Twilio Account Auth Token'

client = Client(account_SID, auth_token)

#display all sent messages
for msg in client.messages.list():
    print(msg.body)

#send new SMS
to = 'to mobile number'
from_ = 'from mobile number'
body = ''hello again using Python :D'

msg = client.messages.create(
    to=to',
    from_=from_,
    body=body,
    )

print(f'Created new message: {msg.sid}')

#deleting all messages
for msg in client.messages.list():
    print(f'Deleting {msg.body}')
    msg.delete()