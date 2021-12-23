# coding:utf-8
import pandas as pd
from pandas import DataFrame
import openpyxl
import os
import xlrd

sheet_names = ['沪A', '沪B', '沪港', '深A', '深B', '深港', '股转A', '股转B']
file = r'D:\git\Python_learning\auto_test\all_excel_cases\JZJY-全量基线模板-案例.xlsx'

wb = xlrd.open_workbook(file)
print(wb.sheet_names())
def read_pre_data_excel(line):  # 使用数据行号来获取对应数据
    df = pd.read_excel(file, sheet_name='数据准备')
    return df.loc[line]


def transfer_map():  # 通过行数来获取带index的值
    pre_data_dict = {}
    df = pd.read_excel(file, sheet_name='数据准备')
    index = list(df.index)
    headers = list(df.columns)
    for each in index:
        data = read_pre_data_excel(each)
        map_dict = dict(zip(headers, data))
        pre_data_dict.setdefault(each + 2, map_dict)
    return pre_data_dict

# map_data = transfer_map()
# print(map_data)

def search_db2(map_data,sql):
    pass


db2_data = {2:
                {
                    4:'00002303',
                    5:'00002306',
                    6:'600000'
                },
            3:
                {
                    4:'01785231',
                    5:'00100710',
                    6:'010107'
                }

            }

def put_pre_data_excel(db2_data):
    workbook = openpyxl.load_workbook(file)
    for line,v in db2_data.items():
        for col,value in v.items():
            workbook['数据准备'].cell(line, col).value = value
    workbook.save(file)

# put_pre_data_excel(db2_data)