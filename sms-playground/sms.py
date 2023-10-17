from twilio.rest import Client

account_sid = 'AC13399f7b5a3b7118a2326b625a1ffe1f'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+17543335525',
    body='HELLLLLOOOOOO',
    to='+5513981292148'
)

print(message.sid)
