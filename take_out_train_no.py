# -*- coding: utf-8 -*-

import xlrd

book = xlrd.open_workbook('Timetable.xls')
sheet = book.sheet_by_index(0)
print(sheet.ncols)
print(sheet.nrows)
ncols = sheet.ncols
nrows = sheet.nrows

for row in range(nrows):
    for col in range(ncols):
        print(sheet.cell_value(col,row))
    
            
#if __name__ == '__main__':
