
#由于要用到软件自带的单元测试框架，这个文件作废，但是也是跑通了的，后面有需要时也可以用到

from test_data import hh_read_excel
from cases  import case1
import sys
class Driven():
   def drive_it(self):
        a=hh_read_excel.Excel()
        table=a.read_it('..\\test_data\\add_excel.xlsx')
        i=1
        for hang in range(1,table.nrows):
            print('\n----Start Test Case'+str(i)+'----')
            list=table.row_values(hang)   #读取到的东西是一个列表，第一行的全部内容

             #获取到里面的每一个参数
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

            moudle=sys.modules['cases.'+list[0]]    #导入模块,需要在类定义的前面也导入，不然在这个地方会报错
            c=getattr(moudle,list[0])             #使用getattr（）这个方法可以得到list[0]这个模块的类，模块名必须和类名相同，否则会报错
            obj=c()                               #实例化这个类，变成一个对象
            method=getattr(obj,list[1])           #根据list[1]得到方法，因为我excel表中方法在第一列，所以list里的数字是1
            method(pro_mame,pro_id,store_nums,weight,sell_price,market_price,cost_price,information,expect) #驱动方法执行，传入测试参数和预期结果
            print('----End Test Case'+str(i)+'----')
            i=i+1

if __name__=='__main__':
     Driven().drive_it()

