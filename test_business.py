from business import getFirstMinute, getLastMinute


class TestBusiness(unittest.TestCase):

    def testIsCorrectFormat(self):
        # Test the path and format of the file
        self.assertTrue(isCorrectFormat("test_Files/test.json"))
        self.assertFalse(isCorrectFormat("test_Files/hanSolo.json"))

    def testIsCorrectFormat(self):
        # Test the path and format of the file
        self.assertIsNotNone(getEvents("test_Files/test.json"))
