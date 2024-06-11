import unittest
from letters import vowel_remove

class VowelRemove(unittest.TestCase):
    def test_vowel_remove(self):
        self.assertEqual(vowel_remove("hello"), "hll")
        self.assertEqual(vowel_remove("world"), "wrld")
        self.assertEqual(vowel_remove("AEIOU"), "")
        self.assertEqual(vowel_remove("abcdefghijklmnopqrstuvwxyz"), "bcdfghjklmnpqrstvwxyz")
        self.assertEqual(vowel_remove(""), "")
        self.assertEqual(vowel_remove("aeiouAEIOU"), "")
        self.assertEqual(vowel_remove("12345"), "12345")
        self.assertEqual(vowel_remove("h3ll0 w0rld"), "h3ll0 w0rld")
            
unittest.main()            