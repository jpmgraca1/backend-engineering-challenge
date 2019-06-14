import unittest
from datetime import datetime, timedelta
from business import getFirstMinute, getLastMinute


class TestBusiness(unittest.TestCase):

    def testgetFirstMinute(self):
        # Test the path and format of the file
        self.assertAlmostEqual(getFirstMinute(
            "2018-12-26 18:11:08.509654"), datetime.strptime("2018-12-26 18:11:00", '%Y-%m-%d %H:%M:%S'))

    def testgetLastMinute(self):
        # Test the path and format of the file
        self.assertAlmostEqual(getLastMinute(
            "2018-12-26 18:11:08.509654", 6), datetime.strptime("2018-12-26 18:17:00", '%Y-%m-%d %H:%M:%S'))
