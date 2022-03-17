# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 21:23:35 2022

@author: ObiraDaniel
"""
import unittest

from translator import englishToFrench, frenchToEnglish

class TestTranslation(unittest.TestCase):
    """Unit test cases for English and French translation"""
    def test_englishtoFrench1(self):
        self.assertEqual(englishToFrench(""), "")

    def test_englishtoFrench2(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

    def test_frenchToEnglish1(self):
        self.assertEqual(frenchToEnglish(""), "")

    def test_frenchToEnglish2(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        
if __name__ == '__main__':
    unittest.main()
