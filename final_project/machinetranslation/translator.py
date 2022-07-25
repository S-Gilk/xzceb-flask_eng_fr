'''
Translation module
'''
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    '''
    Translates English input string and returns French
    '''
    if english_text is None:
        return_string = "None"
    else:
        french_text = language_translator.translate(text= english_text,
        source= "en", target= "fr").get_result()
        return_string = french_text['translations'][0]['translation']
    return return_string

def french_to_english(french_text):
    '''
    Translates French input string and returns English
    '''
    if french_text is None:
        return_string = "None"
    else:
        english_text = language_translator.translate(text= french_text,
        source= "fr", target= "en").get_result()
        return_string = english_text['translations'][0]['translation']
    return return_string
