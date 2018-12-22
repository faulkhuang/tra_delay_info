# -*- coding: utf-8 -*-

#from __future__ import print_fuction
#import sys
import xlrd
#reload(sys)
#sys.setdefaultencoding('utf8')

book = xlrd.open_workbook('AllStationTimeTable.xls')
sheet = book.sheet_by_index(0)
print(sheet.ncols)
print(sheet.nrows)
ncols = sheet.ncols
nrows = sheet.nrows

for row in range(nrows):
    for col in range(ncols):
        cell_value = sheet.cell_value(row, col)
        if cell.ctype in (2,3) and int(cell_value) == cell_value:
            cell_value = int(cell_value)
        else:

#if __name__ == '__main__':
