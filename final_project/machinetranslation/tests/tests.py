import unittest
from translator import englishToFrench, frenchToEnglish


class TestTranslator(unittest.TestCase):

    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello, how are you?'), 'Bonjour, comment allez-vous\xa0?')
        self.assertEqual(englishToFrench('It rains.'), 'Il pleut')
        self.assertEqual(englishToFrench('Hello'), 'Pepitoooo') # The current version translates this
        self.assertNotEqual(englishToFrench('Hello'), 'hi')

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('Bonjour, comment ça va?'), 'Hello, how are you?')
        self.assertEqual(frenchToEnglish('Il pleu.'), "It's raining.")
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Hi')

    def test_emptyString(self):
        self.assertEqual(englishToFrench(''), '')
        self.assertEqual(frenchToEnglish(''), '')

    def test_translationError(self):
        with self.assertRaises(Exception):
            englishToFrench('1234567890')  # Assuming that numbers can't be translated
        with self.assertRaises(Exception):
            frenchToEnglish('1234567890')

if __name__ == '__main__':
    unittest.main()

