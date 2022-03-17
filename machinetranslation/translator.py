import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey="_gW7_yKKuIUY7BjNqAUJONMib9sqw5VaS6tb8ZeXi_a2"
url="https://api.us-south.language-translator.watson.cloud.ibm.com/instances/a96b3dcd-8b2d-42d4-bb9c-fb5104947161"

VERSION='2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """Translates English to French"""
    if englishText == '':
        return ''
    translation_response = language_translator.translate(text=englishText, model_id='en-fr')
    frenchText = translation_response.get_result()['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    """Translates French to English"""
    if frenchText == '':
        return frenchText
    translation_response = language_translator.translate(text=frenchText, model_id='fr-en')
    englishText = translation_response.get_result()['translations'][0]['translation']
    return englishText
