#coding:utf-8

import xlrd
# import xlwt
import xlsxwriter
import time

# excel_read_path = r'C:\\wen he\\hw_selenium1\\txt\\8.7-block.xlsx'
# excel_write_path = r'C:\\wen he\\hw_selenium1\\txt\\8.13-block.xls'


def readExcel(path):
    # 打开工作表
    urls = []
    workbook = xlrd.open_workbook(filename=path)
    # 用索引取第一个工作簿
    booksheet = workbook.sheet_by_index(0)
    # 返回的结果集
    for i in range(booksheet.nrows):
        urls.append(''.join(booksheet.row_values(i)))
    return urls

'''
def set_alignment(flag, color):
    # 样式设置,设置字体居中
    alignment = xlwt.Alignment()  # 创建居中
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # 可取值: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 可取值: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED

    style = xlwt.XFStyle()  # 创建样式
    style.alignment = alignment  # 给样式添加文字居中属性

    if flag == 1:      # 第一列标志位设为1，给第一列添加颜色，其他列不加
        pattern = xlwt.Pattern()  # 设置框的颜色
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        if color == '符合要求':
            pattern.pattern_fore_colour = 3  # 设置框为绿色
        if color == '不符合要求':
            pattern.pattern_fore_colour = 2  # 设置框为红色
        if color == '出现异常':
            pattern.pattern_fore_colour = 5  # 设置框为黄色
        style.pattern = pattern
        return style

    return style


def set_first_row(sheet):
    # 设置列宽
    sheet.col(0).width = 256 * 30
    sheet.col(1).width = 256 * 20
    sheet.col(2).width = 256 * 90
    sheet.col(3).width = 256 * 90
    # 设置行高
    tall_style = xlwt.easyxf('font:height 720')  # 36pt
    sheet.row(0).set_style(tall_style)

    sheet.write(0, 0, 'URL', set_alignment(0, 0))
    sheet.write(0, 1, '结果', set_alignment(0, 0))
    sheet.write(0, 2, 'direct image', set_alignment(0, 0))
    sheet.write(0, 3, 'dcs-proxy image', set_alignment(0, 0))


def writeExcel(path, header, data):
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)

    tall_style = xlwt.easyxf('font:height 1080')  # 54pt
    set_first_row(sheet)

    col = 0
    for row in range(len(header)):
        if data[row] == '出现异常':  # 判断,假如出现异常的话，就把对应的那一行框的高度增加
            sheet.row(row+1).set_style(tall_style)
            sheet.insert_image(row + 1, 2, 'C:/wen he/sana1.jpg')
            sheet.insert_image(row + 1, 3, 'C:/wen he/baidu1.png')
        sheet.write(row+1, col, header[row], set_alignment(1, data[row]))

    col = 1
    for lines in range(len(data)):
        sheet.write(lines+1, col, data[lines], set_alignment(0, 0))


    workbook.save(path)
'''



def writeExcel(path, header, data):

    date = time.strftime('%y-%m-%d', time.localtime())  #获取当地时间
    image1 = r'C:/data/img/%s/direct/' % date
    image2 = r'C:/data/img/%s/dcs-proxy/' % date

    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet('sheet1')

    bold_first_row = workbook.add_format({
        'bold': 1,  # 字体加粗
      # 'fg_color': 'green',  # 单元格背景颜色
        'align': 'center',  # 对齐方式
        'valign': 'vcenter',  # 字体对齐方式
    })
    green = workbook.add_format({'bg_color': 'green', 'align': 'left', 'font_size': 12})
    red = workbook.add_format({'bg_color': 'red', 'align': 'left', 'font_size': 12})
    yellow = workbook.add_format({'bg_color': 'yellow', 'valign': 'vcenter', 'font_size': 12})
    center = workbook.add_format({'align': 'center', 'valign': 'vcenter'})

    worksheet.set_row(0, 50)
    headings = ['URL', '结果', 'direct image', 'dcs-proxy image']
    worksheet.write_row('A1', headings, bold_first_row)  # 首行插入操作

    worksheet.set_column('A:A', 30)
    worksheet.set_column('B:B', 16)
    worksheet.set_column('C:D', 60)

    for row in range(len(header)):
        if data[row] == '出现异常':  # 判断,假如出现异常的话，就把对应的那一行框的高度增加
            worksheet.set_row(row+1, 200)
            worksheet.write(row + 1, 0, header[row], yellow)
            worksheet.insert_image(row + 1, 2, image1+header[row]+'1.png', {'x_scale': 0.5, 'y_scale': 0.3, 'x_offset': 10, 'y_offset': 5})
            worksheet.insert_image(row + 1, 3, image2+header[row]+'2.png', {'x_scale': 0.5, 'y_scale': 0.3, 'x_offset': 10, 'y_offset': 5})

        if data[row] == '符合要求':  # 判断,假如符合要求的话，就把对应的那一行框背景设为绿色
            worksheet.write(row + 1, 0, header[row], green)

        if data[row] == '不符合要求':  # 判断,假如不符合要求的话，就把对应的那一行框背景设为红色
            worksheet.write(row + 1, 0, header[row], red)

        worksheet.write(row+1, 1, data[row], center)

    workbook.close()


'''
date = 'test2'
excel_read_path = r'C:/wen he/hw_selenium1/txt/%s-block.xlsx' % date
excel_write_path = r'C:/wen he/hw_selenium1/txt/%s-result.xls' % date
files = readExcel(excel_read_path)
data = ['出现异常', '符合要求', '不符合要求', '出现异常']
print(files)
writeExcel(excel_write_path, files, data)
'''