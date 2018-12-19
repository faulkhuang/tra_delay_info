# -*- coding: utf-8 -*-

#from __future__ import print_fuction
#import sys
import xlrd
#reload(sys)
#sys.setdefaultencoding('utf8')

book = xlrd.open_workbook('Timetable.xls')
sheet = book.sheet_by_index(0)
print(sheet.ncols)
print(sheet.nrows)
ncols = sheet.ncols
nrows = sheet.nrows

for row in range(nrows):
    for col in range(ncols):
        if isinstance(sheet.cell_value(row, col), int):
            train_no = sheet.cell_value(row, col)
            print(train_no)

#if __name__ == '__main__':
