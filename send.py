from twilio.rest import Client

account_sid = 'AC5f7c454a9cf78c80919f9066e464afdd'
auth_token = 'dbee6b3de8e75f171c654c0ac679ae86'
client = Client(account_sid, auth_token)

def sendSms():
    try:
        message = client.messages.create(
            from_='+12563841322',
            body='Alert',
            to='+8801610840910'
        )
        print("Message SID:", message.sid)
    except Exception as e:
        print("An error occurred:", str(e))

sendSms()
