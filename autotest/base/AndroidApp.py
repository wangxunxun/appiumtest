from autotest.base.core.UI import UI
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class AndroidApp(UI):

    def findElementByClassNameindex(self,classname,index):
        '''
        classname such as 'android.widget.EditView'
        '''
        a=self.driver.find_elements_by_class_name(classname)
        b=a[index - 1]
        return b
    
    def getAllTextView(self):  
        textview=self.driver.find_elements_by_class_name('android.widget.TextView')      
        if textview:
            print('The number of TextView on the page is:%s ' % len(textview))
            i=0
            while i<len(textview):
                print('The %s textview is:%s' % (i+1,textview[i].text))           
                i=i+1 
        else:
            print ('There are no textview')
            
    def getAllButton(self):        
        button=self.driver.find_elements_by_class_name('android.widget.Button')
        if button:
            print('The number of button on the page is:%s ' % len(button))
            i=0
            while i<len(button):
                print('The %s button is:%s' % (i+1,button[i].text))
                i=i+1      
        else:
            print('There are no button')        
    
    def getAllImageView(self):       
        imageview=self.driver.find_elements_by_class_name('android.widget.ImageView')
        if imageview:
            print('The number of imageview on the page is:%s ' % len(imageview))
            i=0
            while i<len(imageview):
                print('The %s imageview is:%s' % (i+1,imageview[i].text))
                i=i+1 
        else:
            print('There are no imageview')
    
    def getAllEditText(self):        
        edittext=self.driver.find_elements_by_class_name('android.widget.EditText')
        if edittext:
            print('The number of edittext on the page is:%s ' % len(edittext))
            i=0
            while i<len(edittext):
                print('The %s edittext is:%s' % (i+1,edittext[i].text))
                i=i+1      
        else:
            print('There are no edittext')
            
    def getAllImageButton(self):        
        imagebutton=self.driver.find_elements_by_class_name('android.widget.ImageButton')
        if imagebutton:
            print('The number of imagebutton on the page is:%s ' % len(imagebutton))
            i=0
            while i<len(imagebutton):
                print('The %s imagebutton is:%s' % (i+1,imagebutton[i].text))
                i=i+1      
        else:
            print('There are no imagebutton')     
            


    def clickBack(self):
        os.system("adb shell input keyevent 4") 
        
    def clickEnter(self):
        os.system("adb shell input keyevent 66") 
        
    def clickHome(self):
        os.system("adb shell input keyevent 3") 
        
    def clickMenu(self):
        os.system("adb shell input keyevent 1") 
        

        
   
        

                     

