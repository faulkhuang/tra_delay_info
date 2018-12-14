import xlwt
import xlrd
from xlutils.copy import copy

def excel_read(doc,table,x,y):
    data=xlrd.open_workbook(Timetable.xls)
    
    