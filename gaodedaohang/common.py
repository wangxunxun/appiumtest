#coding=utf-8
'''
Created on 2015年4月21日

@author: xun
'''
from gaodedaohang import Init_Test
from time import sleep

class common_cases(Init_Test):

    def entermainpage(self):
        sleep(2)
        self.driver.find_element_by_id('com.autonavi.xmgd.navigator:id/checkbox_ignore').click()
        self.driver.find_element_by_id('com.autonavi.xmgd.navigator:id/btn_accept').click()
        sleep(1)
        self.driver.swipe(700, 500, 100, 500, 1000)
        sleep(1)
        self.driver.swipe(700, 500, 100, 500, 1000)
        self.driver.find_element_by_id('com.autonavi.xmgd.navigator:id/guide_btn_end').click()        
        sleep(15)

        
        