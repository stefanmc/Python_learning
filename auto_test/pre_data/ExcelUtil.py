#coding:utf-8
import pandas as pd
from pandas import DataFrame
from openpyxl import load_workbook

import os


sheet_names = ['沪A','沪B','沪港','深A','深B','深港','股转A','股转B']

def read_pre_data_excel(line):  #使用数据行号来获取对应数据
    df = pd.read_excel(r'D:\git\Python_learning\auto_test\all_excel_cases\JZJY-全量基线模板-案例.xlsx', sheet_name='数据准备')
    return df.loc[line]

data = read_pre_data_excel(2)  # 取第三行数据


def put_pre_data_excel(line):
    DataFrame.to_excel(r'D:\git\Python_learning\auto_test\all_excel_cases\JZJY-全量基线模板-案例.xlsx',sheet_name = '数据准备')




