# Importing the translationChallenge function
from translationChallenge import translate
# Importing Twilio's API to make requests to its server
from twilio.rest import TwilioRestClient
# Importing TwilioRestException to code fail safe
from twilio import TwilioRestException


def sendMessage(arrayOfTranslatedText):

    for text in arrayOfTranslatedText:
        # Account SID and Token from Twilio's website
        account_sid = "ACabf12d"
        auth_token = "e060a27e"

        # Creating a client with the SID and Token
        # TwilioRestClient is a function that takes two arguments: account_sid and auth_token
        client = TwilioRestClient(account_sid, auth_token)

        # Arguments for the create method
        receiver = "+13127852285"
        sender = "+13122573902"
        txt = "Here's your translation: " + text

        try:
            """ Creating a message with the Twilio number which will be sent to
                Trevin's phone number. It will send the listOfText which
                contains a list of the return values from the
                translate function. """
            message = client.messages.create(to=receiver, from_=sender, body=txt)
        except TwilioRestException as Error:
            print("Error: Your message cannot be sent.")
            break

    return message.sid

''' translatedTexts is an array of strings as the function translate will
    return two strings '''
translatedTexts = translate(["Hello my name is Cow", "Who are you?",
                             "You loser!", "You shall not pass!"], 'de')

# Calling the function for test
sendMessage(translatedTexts)
