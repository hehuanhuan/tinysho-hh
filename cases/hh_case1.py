from common import hh_group1
import unittest
from test_data import hh_read_excel
from HTMLTestRunner3 import HTMLTestRunner
import time

from test_data import hh_PDBC
class Case1(unittest.TestCase):

    def test_case1(self):
        a=hh_read_excel.Excel()
        table=a.read_it('..\\test_data\\add_excel.xlsx')
        list=table.row_values(1)   #读取到第一行的全部内容,返回的是一个列表
        # 获取到里面的每一个参数
        message=list[2].split('\n')
        print('从excel中查到的商品全部内容是：',message)
        pro_mame=message[0].split(':')[1]
        pro_id=message[1].split(':')[1]
        store_nums=message[2].split(':')[1]
        weight=message[3].split(':')[1]
        sell_price=message[4].split(':')[1]
        market_price=message[5].split(':')[1]
        cost_price=message[6].split(':')[1]
        information=list[3]
        expect=list[4]
        try:
            id=hh_group1.Group1().get_id(pro_mame, pro_id, store_nums, weight, sell_price, market_price, cost_price, information)
            print(id)
            pro_id=hh_PDBC.PDBC().select(pro_id)[0]
            self.assertEqual(id,expect)
            self.assertEqual(id,pro_id)
        except Exception as e:
            print(e)

    def test_case2(self):
        a=hh_read_excel.Excel()
        table=a.read_it('..\\test_data\\add_excel.xlsx')
        list=table.row_values(2)   #读取到第一行的全部内容,返回的是一个列表
        # 获取到里面的每一个参数
        message=list[2].split('\n')
        print(message)
        pro_mame=message[0].split(':')[1]
        print(message[1])
        pro_id=message[1].split(':')[1]
        store_nums=message[2].split(':')[1]
        weight=message[3].split(':')[1]
        sell_price=message[4].split(':')[1]
        market_price=message[5].split(':')[1]
        cost_price=message[6].split(':')[1]
        information=list[3]
        expect=list[4]
        try:
            content1=hh_group1.Group1().get_content1(pro_mame, pro_id, store_nums, weight, sell_price, market_price, cost_price, information)
            print(content1)
            self.assertEqual(content1,expect)
        except Exception as e:
            print(e)
    def test_case3(self):
        a=hh_read_excel.Excel()
        table=a.read_it('..\\test_data\\add_excel.xlsx')
        list=table.row_values(3)   #读取到第一行的全部内容,返回的是一个列表
        # 获取到里面的每一个参数
        message=list[2].split('\n')
        print(message)
        pro_mame=message[0].split(':')[1]
        print(message[1])
        pro_id=message[1].split(':')[1]
        store_nums=message[2].split(':')[1]
        weight=message[3].split(':')[1]
        sell_price=message[4].split(':')[1]
        market_price=message[5].split(':')[1]
        cost_price=message[6].split(':')[1]
        information=list[3]
        expect=list[4]
        try:
            content2=hh_group1.Group1().get_content2(pro_mame, pro_id, store_nums, weight, sell_price, market_price, cost_price, information)
            print(content2)
            self.assertEqual(content2,expect)
        except Exception as e:
            print(e)
    def test_case4(self):
        a=hh_read_excel.Excel()
        table=a.read_it('..\\test_data\\add_excel.xlsx')
        list=table.row_values(4)   #读取到第一行的全部内容,返回的是一个列表
        # 获取到里面的每一个参数
        message=list[2].split('\n')
        print(message)
        pro_mame=message[0].split(':')[1]
        print(message[1])
        pro_id=message[1].split(':')[1]
        store_nums=message[2].split(':')[1]
        weight=message[3].split(':')[1]
        sell_price=message[4].split(':')[1]
        market_price=message[5].split(':')[1]
        cost_price=message[6].split(':')[1]
        information=list[3]
        expect=list[4]
        try:
            id=hh_group1.Group1().get_id(pro_mame, pro_id, store_nums, weight, sell_price, market_price, cost_price, information)
            print(id)
            pro_id=hh_PDBC.PDBC().select(pro_id)[0]
            self.assertEqual(id,expect)
            self.assertEqual(id,pro_id)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    # 用TextTestRunner()执行
    # suite = unittest.TestSuite()
    # suite.addTest(case1('test_case1'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    path = "..\\cases"
    discover = unittest.defaultTestLoader.discover(path, pattern='case1.py')
    current_time = time.strftime("%Y_%m_%d_%H_%M_%S")  #用时间作为测试报告文件名的一部分
    report_path = "..\\report"
    file = open(report_path + "\\" + current_time + "_Report.html", "wb")  #测试报告保存的地址及文件名
    runner = HTMLTestRunner(file, title="商品中心添加功能报告", description="测试环境：win7")
    runner.run(discover)