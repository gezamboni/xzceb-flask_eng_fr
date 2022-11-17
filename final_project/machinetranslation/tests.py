import unittest

from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase): 
    
    def test1(self): 
        #self.assertEqual(french_to_english(''), '')
        self.assertNotEqual(french_to_english("None"), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Hello, how are you')
        self.assertEqual(french_to_english('Bonjour, comment es-tu?'), 'Hello, how are you?')

class TestEnglishToFrench(unittest.TestCase): 
    
    def test1(self): 
        #self.assertEqual(english_to_french(''), '')
        self.assertNotEqual(english_to_french("None"), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Bonjour, comment es-tu?')
        self.assertEqual(english_to_french('Hello, how are you?'), 'Bonjour, comment es-tu?')

unittest.main()