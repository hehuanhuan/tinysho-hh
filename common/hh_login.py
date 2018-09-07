from selenium import webdriver
from time import sleep
from common import hh_setup

class HT_Login():
    def __init__(self,driver):
        self.driver=driver
    def username(self,username):
        self.driver.find_element_by_name('name').clear()
        self.driver.find_element_by_name('name').send_keys(username)
    def password(self,password):
        self.driver.find_element_by_name('password').clear()
        self.driver.find_element_by_name('password').send_keys(password)
    def yz(self):
        self.driver.find_element_by_name('verifyCode').clear()
        self.driver.find_element_by_name('verifyCode').send_keys('aaaa')
    def login(self):
        self.driver.find_element_by_xpath('/html/body/div/div/form/ul/li[4]/input[1]').click()
    def login_go(self,username,password):
        self.username(username)
        self.password(password)
        self.yz()
        self.login()








