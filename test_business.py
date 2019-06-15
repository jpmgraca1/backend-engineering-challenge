import unittest
from datetime import datetime, timedelta
from business import getFirstMinute, getLastMinute, getOutputList


class TestBusiness(unittest.TestCase):

    def testGetFirstMinute(self):
        # Test the path and format of the file
        self.assertAlmostEqual(getFirstMinute(
            "2018-12-26 18:11:08.509654"), datetime.strptime("2018-12-26 18:11:00", '%Y-%m-%d %H:%M:%S'))

    def testGetLastMinute(self):
        # Test the path and format of the file
        self.assertAlmostEqual(getLastMinute(
            "2018-12-26 18:11:08.509654", 6), datetime.strptime("2018-12-26 18:17:00", '%Y-%m-%d %H:%M:%S'))

    def testGetOutputList(self):
        # Test the method that builds the outputlist
        outputlist = getOutputList(datetime.strptime("2018-12-26 18:11:00", '%Y-%m-%d %H:%M:%S'),
                                   datetime.strptime("2018-12-26 18:33:00", '%Y-%m-%d %H:%M:%S'))
        self.assertAlmostEqual(len(outputlist), 23)
