import xlrd
import openpyxl

def read_excel(file_path):
    # 打开excel
    #excel = xlrd.open_workbook(file_path)
    excel = openpyxl.load_workbook(file_path)

    # 获取文件中所有的sheet，通过名字的方式
    #sheet = excel.get_sheet_by_name('哈哈')
    sheet = excel['哈哈']

    # 获取sheet的最大行数和列数
    #rows = sheet.nrows
    #print(rows)
    #cols = sheet.ncols
    #print(cols)

    print('#'*100)
    print(sheet.values)
    print(type(sheet.values))

    # 循环读取每个单元格的值
    #for r in sheet.values:
        #print(r)

    for cell in sheet.values:
            data = {'第一列': cell[0], '第二列': cell[1], '第三列': cell[2]}
            print(data)

if __name__ == '__main__':
    read_excel('/Users/rln/Documents/test_excel.xlsx')


