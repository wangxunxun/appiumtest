#coding=utf-8


import os
import unittest
from selenium.webdriver.common.by import By
from appium import webdriver
from _elementtree import Element
import HTMLTestRunner
import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Init_Test(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['browserName'] = ''
        desired_caps['device'] = 'Android'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.3'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"

        desired_caps['deviceName'] = 'ZTEU930HD'        
        desired_caps['app'] = PATH(
            u'D:/测试APP/Navigator90_9.3_c490_V9.3.8803.1432_20140415.apk'
        )
                
        
        desired_caps['appPackage'] = 'com.autonavi.xmgd.navigator'
        desired_caps['appActivity'] = 'com.autonavi.xmgd.navigator.Warn'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.wait = WebDriverWait(self.driver, 10)        
        


        
    def tearDown(self):
        self.driver.quit()
        
    
