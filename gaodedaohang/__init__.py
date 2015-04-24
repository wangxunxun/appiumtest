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
        
    def findelementbyclassnameindex(self,classname,index):
        a=self.driver.find_elements_by_class_name(classname)
        b=a[index - 1]
        return b
    
    def gettextview(self):  
        textview=self.driver.find_elements_by_class_name('android.widget.TextView')      
        if textview:
            print('The number of TextView on the page is:%s ' % len(textview))
            i=0
            while i<len(textview):
                print('The %s textview is:%s' % (i+1,textview[i].text))           
                i=i+1 
        else:
            print ('There are no textview')
            
    def getbutton(self):        
        button=self.driver.find_elements_by_class_name('android.widget.Button')
        if button:
            print('The number of button on the page is:%s ' % len(button))
            i=0
            while i<len(button):
                print('The %s button is:%s' % (i+1,button[i].text))
                i=i+1      
        else:
            print('There are no button')        
    
    def getimageview(self):       
        imageview=self.driver.find_elements_by_class_name('android.widget.ImageView')
        if imageview:
            print('The number of imageview on the page is:%s ' % len(imageview))
            i=0
            while i<len(imageview):
                print('The %s imageview is:%s' % (i+1,imageview[i].text))
                i=i+1 
        else:
            print('There are no imageview')
    
    def getedittext(self):        
        edittext=self.driver.find_elements_by_class_name('android.widget.EditText')
        if edittext:
            print('The number of edittext on the page is:%s ' % len(edittext))
            i=0
            while i<len(edittext):
                print('The %s edittext is:%s' % (i+1,edittext[i].text))
                i=i+1      
        else:
            print('There are no edittext')
            
