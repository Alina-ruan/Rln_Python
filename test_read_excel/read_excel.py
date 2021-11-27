# coding = utf-8

import xlrd
import pyexcel_xls
import xlwt

def readExcel(file_path):
    # 打开excel
    readbook = xlrd.open_workbook(file_path)
    # 获取文件中所有的sheet，通过名字的方式
    sheet = readbook.sheet_by_name('自定义事件表')

    # 获取sheet的最大行数和列数
    rows = sheet.nrows
    cols = sheet.ncols
    # 循环读取每个单元格的值
    for r in range(1, rows):
        for c in range(1, cols):
            print(sheet.cell(r, c).value)

if __name__ == '__main__':
    readExcel('/Users/rln/Desktop/kmos埋点-商品交易-1118.xlsx')






