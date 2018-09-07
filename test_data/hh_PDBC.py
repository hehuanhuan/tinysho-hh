'''
从数据库返回内容时fetchone()方法和fetchall()方法的区别，并且两个方法不能同时使用，用一个方法获取了数据后，另一个方法再获取时就没有了：
fetchone() ：
返回单个的元组，也就是一条记录(row)，如果没有结果 则返回 None
fetchall() ：
返回多个元组，即返回多个记录(rows),如果没有结果 则返回 ()
'''

import pymysql
class PDBC():
    def __init__(self):
        self.db=pymysql.connect('localhost','root','','tinyshop',charset='utf8')   #实例化之后就直接与数据库连接
        self.cursor=self.db.cursor()   #使用cursor()方法获取操作游标
    def select(self,pro_id):
       try:
            sql="select goods_no from tiny_goods where goods_no='"+pro_id+"'"   #查询表里面的所有商品，查询出来的是一个大元组,元祖里面嵌套元祖
            self.cursor.execute(sql)   #使用execute()方法执行SQL语句
            self.db.commit()    #查询成功后提交到数据库，让数据库执行这条命令
            # self.results=self.cursor.fetchall()   #从后台获取数据库查询后的内容
            # print(self.results[0])
            result = self.cursor.fetchone()  #使用 fetchone() 方法获取一个一维元祖
            print("从数据库获取到的商品编号是 : %s " % result)
            return result
            # self.cursor.close()   #关闭游标
       except Exception as e:
           print(e)
           self.db.rollback()    #抛异常的时候

    # def select2(self):
    #     #查询表里面的所有商品，查询出来的是一个元组
    #     sql='select id from tiny_goods where store_nums=1'
    #     self.cursor.execute(sql)
    #     self.db.commit()
    #     self.results=self.cursor.fetchall()
    #     print(self.results)
    #     self.cursor.close()


    def __del__(self):
        self.cursor.close()   #最后关闭游标
        self.db.close()     #关闭与数据库的连接


if __name__=='__main__':
    a=PDBC()
    a.select('12345')
