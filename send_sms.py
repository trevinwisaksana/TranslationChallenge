# Importing the translationChallenge function
from translationChallenge import translate
# Importing Twilio's API to make requests to its server
from twilio.rest import TwilioRestClient
# Importing TwilioRestException to code fail safe
from twilio import TwilioRestException


def sendMessage(arrayOfTranslatedText):

    for text in arrayOfTranslatedText:
        # Account SID and Token from Twilio's website
        account_sid = "ACabf12db90a28a0be407bd13112d43ec2"
        auth_token = "e060a27eed47fc6c13d4e91f321b4d66"

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
        except TwilioRestException as error:
            print("Error: Your message cannot be sent.")
            print(error)
            break

''' translatedTexts is an array of strings as the function translate will
    return two strings '''
translatedTexts = translate(["What other languages can you speak?"], 'ar')

# Calling the function for test
sendMessage(translatedTexts)
