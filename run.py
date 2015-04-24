#coding=utf-8
'''
Created on 2015年4月20日

@author: xun
'''




import unittest
from test_report import HTMLTestRunner
import datetime


#suite_login = unittest.TestLoader().loadTestsFromTestCase(login)
#suite_setting = unittest.TestLoader().loadTestsFromTestCase(setting)
#alltests =  unittest.TestSuite([suite_login,suite_setting])
test = unittest.TestLoader().loadTestsFromName('gaodedaohang.test_cases.fujin.fujin.test_search')
unittest.TextTestRunner(verbosity=2).run(test)
'''
filename = 'D:/autotestreport/ALE_SERVER_test/testreport_' + datetime.datetime.now().strftime('%Y-%m-%d %H-%M') + '.html' 
fp=file(filename,'wb')
runner = HTMLTestRunner.HTMLTestRunner(
                           stream=fp,
                           title=u'高德导航自动化测试报告',
                           description=u'主要测试登陆、设置两个模块'
                           )
runner.run(test)
'''