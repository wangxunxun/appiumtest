from selenium import webdriver
import unittest, time, re
from time import sleep
import random
import string
import datetime
from selenium.webdriver.support.wait import WebDriverWait
import os




class Initial(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome(executable_path="F:/workplace/appiumtest/testresource/chromedriver.exe", service_args=["--verbose", "--log-path=D:\\qc1.log"])        
        self.wait = WebDriverWait(self.driver, 10)

        
    def tearDown(self):
 
        self.driver.quit()
        
    def fail(self, msg=None):
        """Fail immediately, with the given message."""
        raise self.failureException(msg)
    

    
        