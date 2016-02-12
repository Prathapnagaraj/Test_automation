__author__ = 'pbillava'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import unittest

class test_setting_page(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        self.driver=webdriver.Firefox()
        self.driver.get("http://demo.mahara.org")

    def setUp(self):
        driver=self.driver
        username=WebDriverWait(driver,5).until(lambda driver:driver.find_element_by_id('login_login_username'))
        username.send_keys('student1')
        driver.find_element_by_id('login_login_password').send_keys('Testing1')
        driver.find_element_by_id('login_submit').click()
        if str(driver.title)=='Dashboard - Mahara':
            print "login is sucessfull"
        else:
            print "login is not sucessfull"

    def test_setting_page_1(self):
        driver=self.driver
        driver.find_element_by_link_text('Settings').click()
        maxtag=WebDrivrWait(driver,10).until(lambda driver:driver.find_element_by_xpath('//div/input[@id="accountprefs_groupsideblockmaxgroups"]'))
        maxtag.send_keys(30)
        driver.find_element_by_id('accountprefs_submit').click()
        max_text

    def tearDown(self):
        driver=self.webdriver
        driver.find_element_by_link_text('Logout').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

