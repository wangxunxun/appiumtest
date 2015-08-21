'''
Created on 2015年8月21日

@author: xun
'''
from autotest.base.WebApp import WebApp


class test(WebApp):
    def test_nopassword(self):
        print(1111)
        self.driver.get('baidu.com')
        print(1111)