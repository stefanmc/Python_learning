# coding:utf-8
import pandas as pd
from pandas import DataFrame
import openpyxl
import os

sheet_names = ['沪A', '沪B', '沪港', '深A', '深B', '深港', '股转A', '股转B']


def read_pre_data_excel(line):  # 使用数据行号来获取对应数据
    df = pd.read_excel(r'/Users/stephen/Desktop/git/Python_learning/auto_test/all_excel_cases/JZJY-全量基线模板-案例.xlsx',
                       sheet_name='数据准备')
    return df.loc[line]


def put_pre_data_excel(line):
    pass


def transfer_map(line):  # 通过行数来获取带index的值
    pre_data_dict = {}
    df = pd.read_excel(r'/Users/stephen/Desktop/git/Python_learning/auto_test/all_excel_cases/JZJY-全量基线模板-案例.xlsx',
                       sheet_name='数据准备')
    # index = list(df.index)
    headers = list(df.columns)
    # for each in index:
    data = read_pre_data_excel(line)
    map_dict = dict(zip(headers, data))
    pre_data_dict.setdefault(line, map_dict)
    return pre_data_dict


print(transfer_map(2))











