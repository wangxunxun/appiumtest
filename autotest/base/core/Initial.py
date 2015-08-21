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
#        self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome(executable_path="C:/Users/xun/workspace/appiumtest/testresource/chromedriver.exe", service_args=["--verbose", "--log-path=D:\\qc1.log"])        
#        self.driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe", service_args=["--verbose", "--log-path=D:\\qc1.log"])
#        self.driver = webdriver.Remote("http://localhost:8080/wd/hub", webdriver.DesiredCapabilities.ANDROID)
        self.driver.implicitly_wait(30)
        self.wait = WebDriverWait(self.driver, 10)

        
    def tearDown(self):
 
        self.driver.quit()
        
currentpath = os.path.dirname(__file__).replace("\\","/")
os.path.join(os.path.dirname(__file__), "app/templates")