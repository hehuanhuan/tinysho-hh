from selenium import webdriver
class Setup():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)
        self.driver.get('http://localhost/TinyShop/admin')

