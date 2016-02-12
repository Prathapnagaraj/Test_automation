__author__ = 'pbillava'

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Mylogintest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()

    def test_login(self):
        driver=self.driver
        driver.get("http://demo.mahara.org")
        self.assertIn("Home - Mahara", driver.title)
        user_name=driver.find_element_by_id('login_login_username')
        pass_word=driver.find_element_by_id('login_login_password')
        user_name.send_keys('student1')
        pass_word.send_keys('Testing1')
        login_button=driver.find_element_by_id('login_submit')
        login_button.click()
        self.assertIn('Dashboard - Mahara', driver.title)
        print "login is sucessfull"

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ =='__main__':
    unittest.main(verbosity=2)


