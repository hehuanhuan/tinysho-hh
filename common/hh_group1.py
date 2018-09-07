from selenium import webdriver
from common import hh_setup
from common import hh_login
from common import hh_product_manage
class Group1():
    def __init__(self):
        self.driver=hh_setup.Setup().driver
        hh_login.HT_Login(self.driver).login_go('admin', 'admin123')
        self.a=hh_product_manage.Product_Manage(self.driver)

    def get_id(self,pro_mame,pro_id,store_nums,weight,sell_price,market_price,cost_price,information):
        try:
            self.a.add_go(pro_mame,pro_id,store_nums,weight,sell_price,market_price,cost_price,information)
            self.id=self.driver.find_element_by_css_selector('td[style="width:80px;"]').text
            print(self.id)
            return self.id
        except Exception as e:
            print(e)

    def get_content1(self,pro_mame,pro_id,store_nums,weight,sell_price,market_price,cost_price,information):
        try:
            self.a.add_go(pro_mame,pro_id,store_nums,weight,sell_price,market_price,cost_price,information)
            # content1=self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/div/div[1]/div[1]/dl[8]/dd/label').text
            content1=self.driver.find_element_by_css_selector("label[class='invalid-msg']").text
            print(content1)
            return content1
        except Exception as e:
            print(e)

    def get_content2(self,pro_mame,pro_id,store_nums,weight,sell_price,market_price,cost_price,information):
        try:
            self.a.add_go(pro_mame,pro_id,store_nums,weight,sell_price,market_price,cost_price,information)
            # content2=self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/div/div[1]/div[1]/div[1]/table/thead/tr[4]/td[2]/label').text
            content2=self.driver.find_element_by_css_selector("label[class='invalid-msg']").text
            print(content2)
            return content2
        except Exception as e:
            print(e)


    # def get_content3(self,pro_mame,pro_id,store_nums,weight,sell_price,market_price,cost_price,information):
    #     try:
    #         # self.a.add_go(pro_mame,pro_id,store_nums,weight,sell_price,market_price,cost_price,information)
    #
    #         id=self.driver.find_element_by_css_selector('td[style="width:80px;"]').textcontent3=self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/div/div[1]/div[1]/div[1]/table/thead/tr[4]/td[2]/label').text
    #         print(id)
    #         return id
    #     except Exception as e:
    #         print(e)