from selenium import webdriver
import os
import time
cd="chromedriver.exe"
class InstaBot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.driver=webdriver.Chrome(cd)
        self.login()
    def login(self):
            
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        time.sleep(1)
        self.driver.find_elements_by_xpath("//div[contains(text(),'Log In')]")[0].click()
        time.sleep(10)
        self.driver.get("https://www.instagram.com/emmawatson/")
        Follow_Button = self.driver.find_element_by_xpath("//*[text()='Follow']")
        Follow_Button.click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[text()='Follow']").click()  
        x=20
        while x > 0: 
            self.driver.find_element_by_xpath("//*[text()='Follow']").click() 
            
            time.sleep(5)
            self.driver.find_element_by_xpath("//*[text()='Cancel']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[text()='Follow']").click() 
            time.sleep(1)
            
            self.driver.find_element_by_xpath("//*[text()='Follow']").click()
            time.sleep(5)
            self.driver.find_element_by_xpath("//*[text()='Follow']").click() 
            
            
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[text()='Follow']").click()
            
            
            x=x-1
            break
        

    def nav_user(self,username):
        name="username"
        self.driver.get('https;//instagram.com/'+name)    
if __name__=='__main__':
    igbot=InstaBot('username','pw')

    print(igbot.username)
