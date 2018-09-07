from test_data import hh_read_excel
import xlrd
class Data():
    def datas(self):
        table=hh_read_excel.Excel().read_it('..\\test_data\\add_excel.xlsx')
        for hang in range(1,table.nrows):
            all=table.row_values(hang)[2].split('\n')
            print(all)
            pro_mame=all[0].split(':')[1]
            pro_id=all[1].split(':')[1]
            store_nums=all[2].split(':')[1]
            weight=all[3].split(':')[1]
            sell_price=all[4].split(':')[1]
            market_price=all[5].split(':')[1]
            cost_price=all[6].split(':')[1]
            information=table.row_values(hang)[3]
            expect=table.row_values(hang)[4]


if __name__=='__main__':
    Data().datas()