'''This is a file which contains functions for translations'''

from deep_translator import MyMemoryTranslator


def englishToFrench(english_text):
    '''Translates a provided English text into French'''
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text


def frenchToEnglish(french_text):
    '''Translates a provided French text into English'''
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
