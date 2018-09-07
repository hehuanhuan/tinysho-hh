import xlrd
class Excel():
    def read_it(self,file,index=0):
        data=xlrd.open_workbook(file)
        sheet=data.sheets()[index]
        return sheet
