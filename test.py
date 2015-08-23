'''
Created on 2015年8月21日

@author: xun
'''
from autotest.base.WebApp import WebApp
import unittest
from time import sleep
from autotest.utils.ReadExcel import ReadSelectData,ReadTestCaseData
from selenium import webdriver
import unittest, time, re
from time import sleep
import random
import string
import datetime
from selenium.webdriver.support.wait import WebDriverWait
import os
from autotest.test_report import HTMLTestRunner

currentpath = os.path.dirname(__file__).replace("\\","/")
class test(WebApp):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="F:/workplace/appiumtest/testresource/chromedriver.exe", service_args=["--verbose", "--log-path=D:\\qc1.log"])        
        self.wait = WebDriverWait(self.driver, 10)
        aa = ReadSelectData(currentpath +'/testresource/test.xls','Sheet1')
        self.data = aa.getdata()
    
    def test_nopassword(self):
        self.enter('http://baidu.com')
#        self.driver.find_element_by_id('444')
        self.findElement(self.data, '主页', '搜索输入框').send_keys('333333')
        self.findElement(self.data, '主页', '搜索按钮').click()
        aa = ReadTestCaseData(currentpath +'/testresource/test.xls','Sheet2')
        print(aa.readTable())
        sleep(3)
#        self.assertEqual('333', '45', '55')
        
        
if __name__ == "__main__":
    suite_setting = unittest.TestLoader().loadTestsFromTestCase(test)


    unittest.TextTestRunner(verbosity=2).run(suite_setting)
    
'''
    filename = 'D:/testreport_' + datetime.datetime.now().strftime('%Y-%m-%d %H-%M') + '.html' 
#    filename = 'D:/autotestreport/ALE_SERVER_test/testreport_' + datetime.datetime.now().strftime('%Y-%m-%d %H-%M') + '.html' 
    fp = open(filename,'w',encoding = "utf-8")

    runner = HTMLTestRunner.HTMLTestRunner(
                               stream=fp,
                               title='ALE server',
                               description='Report_description'
                               )
    runner.run(suite_setting)
'''