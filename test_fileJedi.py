import unittest
from datetime import datetime, timedelta
from pathlib import Path
from fileJedi import isCorrectFormat, getEvents, writeOutputFile


class TestFileJedi(unittest.TestCase):

    def testIsCorrectFormat(self):
        # Test the path and format of the file
        self.assertTrue(isCorrectFormat("test_Files/test.json"))
        self.assertFalse(isCorrectFormat("test_Files/hanSolo.json"))

    def testIsCorrectFormat(self):
        # Test the path and format of the file
        self.assertIsNotNone(getEvents("test_Files/test.json"))

    def testWriteOutputFile(self):
        outputList = []
        outputList.insert(0, {'date': datetime.strptime(
            "2018-12-26 18:11:00", '%Y-%m-%d %H:%M:%S'), 'average_delivery_time': 0.0})
        writeOutputFile(outputList, "test_Files/finalOutput.json")
        path = Path("test_Files/finalOutput.json")

        self.assertTrue(path.exists())
