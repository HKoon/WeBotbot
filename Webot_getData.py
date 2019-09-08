# -*- coding: UTF-8 -*-
import xdrlib ,sys
import os
import xlrd
import xlwt
from collections import defaultdict
#from xlutils.copy import copy  #修改字典dataDict后再写入新建的一个excel表覆盖保存，与此库功能没有本质区别

#打开excel文件
def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的索引   by_name：Sheet1名称
def get_dataDict(file, colnameindex, by_name):
    if not os.path.isfile(file):
        file = input("未找到配表,请手动将表格拖进来:") 
    data = open_excel(file) #打开excel文件
    table = data.sheet_by_name(by_name) #根据sheet名字来获取excel中的sheet
    nrows = table.nrows #行数 
    colnames = table.row_values(colnameindex) #某一行数据 
    dataDict = defaultdict(list) #装读取结果的序列
    for rownum in range(0, nrows): #遍历每一行的内容
        row = table.row_values(rownum) #根据行号获取行
        varName = row[0]
        if row: #如果行存在
            for i in range(len(colnames)-1): #一列列地读取行的内容
                if row[i+1]:
                    dataDict[varName].append(row[i+1])
    return dataDict

def update_dataDict(file, dataDict):
    if not os.path.isfile(file):
        file = input("未找到配表,请手动将表格拖进来:")
    workbook = xlwt.workbook()
    worksheet = workbook.add_sheet("setting")
    row = 0
    for key, values in dataDict.items():
        worksheet.write(row, 0, key)
        col = 1
        for value in values:
            worksheet.write(row, col, value)
            col += 1
        row += 1
    try:
        os.remove(file)
        workbook.save(file)
    except Exception as e:
        print(str(e))

