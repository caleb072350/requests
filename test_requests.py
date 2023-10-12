
import unittest

import myrequests.core 

class MyRequestsTestSuite(unittest.TestCase):
    """Requests test cases."""

    def setUp(self):
        pass 
    
    def tearDown(self):
        """Testdown."""
        pass

    def test_invalid_url(self):
        self.assertRaises(ValueError, myrequests.core.get, 'hiwpefhipowhefopw')

    def test_HTTP_200_OK_GET(self):
        r = myrequests.core.get('http://www.baidu.com')
        self.assertEqual(r.status_code, 200)
    
    def test_HTTPS_200_OK_GET(self):
        r = myrequests.core.get('https://www.baidu.com')
        self.assertEqual(r.status_code, 200)
    
    def test_HTTP_200_OK_HEAD(self):
        r = myrequests.core.head('http://www.baidu.com')
        self.assertEqual(r.status_code, 200)
    
    def test_HTTPS_200_OK_HEAD(self):
        r = myrequests.core.head('https://www.baidu.com')
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()
