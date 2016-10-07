from translationChallenge import translate
from twilio.rest import TwilioRestClient

# Twillio
POST_URL = 'https://www.twilio.com/docs/quickstart/python/sms/sending-via-rest'

# Download the twilio-python library from http://twilio.com/docs/libraries

# Find these values at https://twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXX"
auth_token = "YYYYYYYYYYYYYYYYYY"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+12316851234", from_="+15555555555", body=translate.outputArray)
