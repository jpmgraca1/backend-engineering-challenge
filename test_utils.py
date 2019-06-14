import unittest
from utils import verifyArgumentsNumber, extractFileName, extractWindowSize


class TestUtils(unittest.TestCase):
    def testArgumentNumber(self):
        # Test the argument number verification
        self.assertTrue(verifyArgumentsNumber(3))
        self.assertFalse(verifyArgumentsNumber(1))
        self.assertFalse(verifyArgumentsNumber(4))

    def testExtractFileName(self):
        # Test the File Name extraction
        self.assertIsNone(extractFileName("numbers.pdf"))
        self.assertIsNone(extractFileName("numbers"))
        self.assertAlmostEqual(
            extractFileName("events.json"), "events.json")

    def testExtractWindowSize(self):
        # Test the Window Size extraction
        self.assertAlmostEqual(extractWindowSize("3"), 3)
        self.assertIsNone(extractWindowSize("3.5"))
        self.assertIsNone(extractWindowSize("darth maul"))
