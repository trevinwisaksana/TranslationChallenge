# This library has to be imported so that we can use this to make requests
import httplib2
# Included so that we don't have to add ASCII to add spaces
import urllib
# For conversion of HTMl into JSON
import json

'''
Challenges:
1. Create a Python wrapper function for Translate:
    print translate_text) -> translate_text

2. Extended your wrapper function with target language:
    print translate(text, language='XX') -> text in XX language

3. Extended your wrapper function to translate multiple strings:
    print translate([text1, text2, ...], language='XX')
    -> [text1 in XX language, text 2 in XX language, ...]

4. Add Twilio SMS functionality to text the translation to you!
'''


def translate(arrayOfText, language):
        # Empty array which will store the appended texts
        outputArray = []

        # This is the text that will be translated
        ''' Key has to be included in the URL so that we can get permission to
            be granted '''
        GOOGLE_API_KEY = "AIzaSy"
        TRANSLATE_URL = 'https://www.googleapis.com/language/translate/v2'
        partial_url = TRANSLATE_URL + '?key=' + GOOGLE_API_KEY + '&source=en&target=' + language

        for text in arrayOfText:
            ''' The text cannot be translated if there's space on the text.
                Usually, we have to use %20. But this is not user friendly. But
                by using urlib.quote_plus(text) this will allow the computer to
                understand the spaces without using ASCII on the UI.
            '''
            text_encoded = urllib.quote_plus(text)

            ''' url concatenates both the googleapis url and the text that is encoded
                that does not have to accept ASCII spaces.'''
            url = partial_url + '&q=' + text_encoded
            # url = partial_url + '&q=' + text  # Google returns HTML instead of JSON

            ''' Http is a class that is part of the httplib2 method. '''
            http = httplib2.Http()

            ''' We then send two arguments on the request method. "GET" is a command
                understood by http.'''
            response, body = http.request(url, "GET")

            # Testing if the return value is in JSON format
            try:
                parsed_body = json.loads(body)
            except Exception as error:
                print('Translation failed with no JSON response from Google.')
                break

            # Testing if the parsed_body contains data or is an error
            try:
                tryData = parsed_body['data']
            except Exception as error:
                print("Error: Translation failed due to bad request.")
                break

            # Retreive translated text from the first index which is index[0]
            translatedText2 = parsed_body['data']['translations'][0]['translatedText']
            # Text is appended to the outputArray
            outputArray.append(translatedText2)
            # Prints out the orignial text and the translated text in human format
            print(text + " translates to " + translatedText2)

        # Returns the outputArray which ends the for loop to end the function
        return outputArray
