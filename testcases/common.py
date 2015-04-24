#coding=utf-8
'''
Created on 2015年4月21日

@author: xun
'''
from testcases import Init_Test
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