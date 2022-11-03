import unittest
from Scraperdir.loader import Loader

class TestLoader(unittest.TestCase):
    def setUp(self) -> None:
        pass
        
# TODO test to see the presence of the raw data file

    def testDirectoryExists(self):
        import os
        self.assertTrue(os.path.exists("C:\\Users\\awoye\\OneDrive\\Documents\\GitHub\\data-collection-pipeline782//raw_data"))