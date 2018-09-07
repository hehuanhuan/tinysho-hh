import unittest
from HTMLTestRunner3 import HTMLTestRunner
import time

#相对路径
path = "..\\cases"
discover = unittest.defaultTestLoader.discover(path, pattern='hh_case1.py')


if __name__ == "__main__":
    #用TextTestRunner()执行
    # runner = unittest.TextTestRunner()
    # runner.run(discover)

    #用HTMLTestRunner()执行
    current_time = time.strftime("%Y_%m_%d_%H_%M_%S")  #用时间作为测试报告文件名的一部分
    report_path = "..\\report"
    file = open(report_path + "\\" + current_time + "_TestReport.html", "wb")  #测试报告保存的地址及文件名
    runner = HTMLTestRunner(file, title="登录报告", description="测试环境：win7")
    runner.run(discover)