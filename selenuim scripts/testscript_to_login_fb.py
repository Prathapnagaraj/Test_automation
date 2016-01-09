__author__ = 'pbillava'
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest

class logintest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("http://www.facebook.com")

    def test_login(self):
        driver=self.driver
        fb_username="prathapn054@gmail.com"
        fb_pass="4Mc08ec054#1990"
        emailField="email"
        passField="pass"
        loginButton="//input[@value='Log In']"
        fb_logo='(//a[contains(@href,"logo")][1])'
        email=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(emailField))
        passw=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(passField))
        #import time
        #time.sleep(10)
        email.clear()
        email.send_keys(fb_username)
        passw.clear()
        passw.send_keys(fb_pass)
        login_bot=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(loginButton))
        login_bot.click()
        WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_xpath(fb_logo))


if __name__=='__main__':
    unittest.main()