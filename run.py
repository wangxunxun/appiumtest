#coding=utf-8
'''
Created on 2015年4月20日

@author: xun
'''




import unittest





#suite_login = unittest.TestLoader().loadTestsFromTestCase(login)
#suite_setting = unittest.TestLoader().loadTestsFromTestCase(setting)
#alltests =  unittest.TestSuite([suite_login,suite_setting])
test = unittest.TestLoader().loadTestsFromName('gaodedaohang.fujin.fujin.test_login')
unittest.TextTestRunner(verbosity=2).run(test)