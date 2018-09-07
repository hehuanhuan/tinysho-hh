from selenium import webdriver
from time import sleep
class Product_Manage():
    def __init__(self,driver):
        self.driver=driver
        # sleep(1)
        self.driver.find_element_by_link_text('商品中心').click()
        # sleep(1)
        self.driver.find_element_by_link_text('商品管理').click()
        self.driver.find_element_by_link_text('添加').click()
     #添加基本信息
    def add_jiben(self,pro_mame,pro_id,store_nums,weight,sell_price,market_price,cost_price):
        #分类
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/div/div[1]/div[1]/dl[2]/dd/select/option[3]').click()
        #商品名称
        self.driver.find_element_by_name('name').clear()
        self.driver.find_element_by_name('name').send_keys(pro_mame)
        #商品编号
        self.driver.find_element_by_name('goods_no').clear()
        self.driver.find_element_by_name('goods_no').send_keys(pro_id)
        #上架
        self.driver.find_element_by_name('is_online').click()
        #产品相册
        #点击添加图片按钮
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/div/div[1]/div[1]/dl[10]/dd/button').click()
        #跳转
        self.driver.switch_to.frame(self.driver.find_element_by_name('Openupimg_dialog'))
        self.driver.find_element_by_name('upfile').send_keys('C:\\Users\\Administrator\\Desktop\\40.jpg')
        self.driver.find_element_by_xpath('/html/body/div[3]/button').click()
        #跳出
        self.driver.switch_to.default_content()
        #库存
        self.driver.find_element_by_name('store_nums').clear()
        self.driver.find_element_by_name('store_nums').send_keys(store_nums)
        #重量
        self.driver.find_element_by_name('weight').clear()
        self.driver.find_element_by_name('weight').send_keys(weight)
        #零售价
        self.driver.find_element_by_name('sell_price').clear()
        self.driver.find_element_by_name('sell_price').send_keys(sell_price)
        #市场价
        self.driver.find_element_by_name('market_price').clear()
        self.driver.find_element_by_name('market_price').send_keys(market_price)
        #成本价
        self.driver.find_element_by_name('cost_price').clear()
        self.driver.find_element_by_name('cost_price').send_keys(cost_price)
        sleep(2)

        #新增描述信息
    def add_miaoshu(self,information):
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/div/ul/li[2]').click()
        #跳到文本框里写文本
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/div/div[1]/div[2]/div/div/div[2]/iframe'))
        self.driver.find_element_by_xpath('/html/body').send_keys(information)
        self.driver.switch_to.default_content()

    #提交
    def submit(self):
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/div/div[2]/input[1]').click()

    #上架
    # def shangjia(self):
    #     # self.driver.find_element_by_xpath("//input[@value='33']").click()
    #     self.driver.find_element_by_name('id[]').click()
    #     self.driver.find_element_by_link_text('上架').click()


    def add_go(self,pro_mame,pro_id,store_nums,weight,sell_price,market_price,cost_price,information):
        self.add_jiben(pro_mame,pro_id,store_nums,weight,sell_price,market_price,cost_price)
        self.add_miaoshu(information)
        self.submit()
        # self.shangjia()
