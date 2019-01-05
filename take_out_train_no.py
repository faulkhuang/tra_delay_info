# -*- coding: utf-8 -*-
import os
import pandas
import xlrd

book = xlrd.open_workbook('AllStationTimeTable.xls', logfile=open(os.devnull, 'w'))
#pd.read_excel(book)
sheet = book.sheet_by_index(0)
print(sheet.ncols)
print(sheet.nrows)
ncols = sheet.ncols
nrows = sheet.nrows

for col in range(ncols):
    for row in range(nrows):
        cell_value = sheet.cell_value(row, col)
        if not cell_value:
            pass
        else:
            try:
                int(cell_value)
                print(cell_value)
            except:
                pass
#        else:
#            pass

#if __name__ == '__main__':
