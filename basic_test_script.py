###############################33
#
# Comment about script
#
###############################
'''
import all libraries
'''
import unittest
import logging
logging.basicConfig(level=logging.DEBUG)
log=logging.getLogger(__name__)
class Basic_test_class(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log.info("hello setupclass")
        print "Doing set up first at setUpClass"

    def setUp(self):
        log.info("hello setup")
        print "instant set up"

    def test1(self):
        print "testcase 1"
        log.info('test1')

    def test2(self):
        print "testcase 2"
        log.info('test2')

    def tearDown(self):
        print "instant teardown"
        log.info('hello teardown')

    @classmethod
    def tearDownClass(cls):
        log.info('hello teardown class')
        print "Doing tearndown at teardown class"

if __name__=="__main__":
    unittest.main()







__author__ = 'pbillava'
