import unittest
from fileJedi import isCorrectFormat, getEvents


class TestFileJedi(unittest.TestCase):

    def testIsCorrectFormat(self):
        # Test the path and format of the file
        self.assertTrue(isCorrectFormat("test_Files/test.json"))
        self.assertFalse(isCorrectFormat("test_Files/hanSolo.json"))
