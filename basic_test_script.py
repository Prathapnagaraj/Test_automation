###############################33
#
# Comment about script
#
###############################
'''
import all libraries
'''
import unittest
class Basic_test_class(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "Doing set up first at setUpClass"

    def setUp(self):
        print "instant set up"

    def test1(self):
        print "testcase 1"

    def test2(self):
        print "testcase 2"

    def tearDown(self):
        print "instant teardown"

    @classmethod
    def tearDownClass(cls):
        print "Doing tearndown at teardown class"

if __name__=="__main__":
    unittest.main()







__author__ = 'pbillava'
