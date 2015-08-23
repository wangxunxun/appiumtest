from autotest.base.core.Initial import Initial
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class UI(Initial):
    def inputByEle(self,content,ele):
        i=1            
        while (i<3):
            ele.clear()
            i=i+1
        
        ele.send_keys(content)  
        
    def waitUntilElementByID(self,eleid):
        self.wait.until(EC.presence_of_element_located((By.ID,eleid)))
        
    def inputById(self,content,eleid):
        
        ele = self.driver.find_element_by_id(eleid)
        i=1            
        while (i<3):
            ele.clear()
            i=i+1
        
        ele.send_keys(content)   
        
    def swipeByType(self,swipetype):
        windowlenX = self.driver.get_window_size().get('width')
        windowlenY = self.driver.get_window_size().get('height')
        if (swipetype == 'Left'):
            self.driver.swipe((int) (windowlenX * 0.9), (int) (windowlenY * 0.5), (int) (windowlenX * 0.2), (int) (windowlenY * 0.5),
                    3000);

        if (swipetype == 'Right'):
            self.driver.swipe((int) (windowlenX * 0.2), (int) (windowlenY * 0.5), (int) (windowlenX * 0.9), (int) (windowlenY * 0.5),
                    3000);
                    
        if (swipetype == 'Down'):

            self.driver.swipe((int) (windowlenX * 0.5), (int) (windowlenY * 0.4), (int) (windowlenX * 0.5), (int) (windowlenY * 0.9),
                        3000);
     
        if (swipetype == 'Up'):

            self.driver.swipe((int) (windowlenX * 0.5), (int) (windowlenY * 0.9), (int) (windowlenX * 0.5), (int) (windowlenY * 0.4),
                        3000);
                        
    def findElement(self,data,page,name):
        selectType =data.get(page).get(name).get('SelectType')
        location = data.get(page).get(name).get('Location')
        if selectType == 'id':
            return self.driver.find_element_by_id(location)
        if selectType == 'css':
            return self.driver.find_element_by_css_selector(location)
        if selectType == 'xpath':
            return self.driver.find_element_by_xpath(location)
        else:
            print('No surpport')