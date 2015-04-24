#coding=utf-8
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .. import common

class fujin(common.common_cases):
    
    def test_login(self):
        self.entermainpage()
        self.gettextview()

        
        
        self.driver.swipe(500,500, 300,500,1000)
        sleep(2)
        self.driver.find_element_by_id('com.autonavi.xmgd.navigator:id/map_tool_bar_nearby_text').click()
        self.getbutton()
        self.getedittext()
        self.getimageview()
#        self.driver.find_element_by_name(u'加油站').click()    
        self.findelementbyclassnameindex('android.widget.ImageView', 2).click()
        self.driver.find_element_by_name(u'导航').click()
        sleep(4)

        self.assertTrue(self.driver.find_element_by_name(u'模拟导航'), "failed")
        
        
        sleep(4)
    
    def test_search(self):
        self.entermainpage()
        self.driver.swipe(500,500, 300,500,1000)
        self.wait.until(EC.presence_of_element_located((By.ID,'com.autonavi.xmgd.navigator:id/map_title_searchbar')))
        self.driver.find_element_by_id('com.autonavi.xmgd.navigator:id/map_title_searchbar').click()
        self.driver.find_element_by_id('com.autonavi.xmgd.navigator:id/search_edit').send_keys(u"武汉")

        self.driver.find_element_by_id('com.autonavi.xmgd.navigator:id/make_sure_search').click()
        sleep(3)
        self.getbutton()
        self.gettextview()
        self.getedittext()
        self.getimageview()
        self.getimagebutton()
        self.driver.get_screenshot_as_file('D:/autotestreport/search%s.png' %datetime.datetime.now().strftime('%Y-%m-%d %H-%M'))
        sleep(8)