__author__ = 'pbillava'
from selenium import webdriver
import unittest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select



class dropdowntest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://www.facebook.com")

    def test_dropdown(self):
        driver=self.driver
        dropd=WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_id('month'))
        Select(dropd).select_by_visible_text("May")
        import time
        time.sleep(10)

    def tearDown(self):
        self.driver.close()
