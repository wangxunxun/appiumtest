'''
Created on 2015年8月22日

@author: wangxun
'''
from autotest.base.AndroidApp import AndroidApp
import unittest
from appium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
import os

class antest(AndroidApp):
    def setUp(self):
        desired_caps = {}
        desired_caps['browserName'] = ''
        desired_caps['device'] = 'Android'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.3'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"

        desired_caps['deviceName'] = 'ZTEU930HD'        
        desired_caps['app'] = u"F:/workplace/appiumtest/testresource/apps/MainActivity.apk"

                

        desired_caps['appPackage'] = 'com.example.testandroid'
        desired_caps['appActivity'] = 'com.example.testandroid.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.wait = WebDriverWait(self.driver, 20)      
        
    def test_aa(self):
#        sleep(111)  
        self.driver.find_element_by_id('edittext').click()
        self.getAllEditText()
        ele = self.findElementByClassNameindex('android.widget.EditText', 1)
        ele.send_keys('111')
        self.inputByEle('33344445555', ele)
        sleep(12)
        

        
        

        
        
if __name__ == "__main__":
    suite_setting = unittest.TestLoader().loadTestsFromTestCase(antest)


    unittest.TextTestRunner(verbosity=2).run(suite_setting)
        
