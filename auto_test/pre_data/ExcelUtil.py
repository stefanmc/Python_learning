# coding:utf-8

import openpyxl
import xlrd
import analyze_pre_data as apd
import os
from tools.read_yml import PyrunConfig

sheet_names = ['沪A', '沪B', '沪港', '深A', '深B', '深港', '股转A', '股转B']
file = r'F:\11-开发项目\pyrun_rebuild\pyrun_rebuild\all_excel_cases\JZJY-全量基线模板-案例.xlsx'
sql_path = r'F:\11-开发项目\pyrun_rebuild\pyrun_rebuild\SQL\SQL_JZJY'


def load_pre_data_excel():  # 读取pre_data excel 数据
    wb = xlrd.open_workbook(file)
    pre_data = wb.sheet_by_name('数据准备')
    pre_data_dict = {}
    headers = pre_data.row_values(0)  # excel headers
    row_list = [i for i in range(1, pre_data.nrows)]  # 数据行
    for each in row_list:
        data = pre_data.row_values(each)
        map_dict = dict(zip(headers, data))
        pre_data_dict.setdefault(each + 1, map_dict)

    return pre_data_dict


def filter_pre_data(pre_data: dict) -> dict:
    '''
    :param pre_data:
    :return: dict
    '''
    filter_dict = {}
    for k, v in pre_data.items():
        if v.get('是否准备数据').strip() == '是':
            filter_dict.setdefault(k, v)

    return filter_dict


def search_db2(map_data, sql):
    pass


def put_pre_data_excel(db2_data):
    workbook = openpyxl.load_workbook(file)
    for line, v in db2_data.items():
        for col, value in v.items():
            workbook['数据准备'].cell(line, col).value = value
    workbook.save(file)


if __name__ == "__main__":
    from pyrun_rebuild.DB2 import db_pool
    from pyrun_rebuild.DB2 import process_db2

    app_cfg = PyrunConfig('app_config.yml')
    business_cfg = PyrunConfig('business_config.yml')
    data_source, detail = app_cfg.read_app_config()
    business = business_cfg.read_business_config()

    DB2_DICT = {}
    DB2_DICT['uid'] = 'jzjybcc'
    DB2_DICT['password'] = 'y2iaciej'
    DB2_DICT['host'] = data_source['MAIN_DB2']['ip']
    DB2_DICT['port'] = data_source['MAIN_DB2']['port']
    DB2_DICT['database'] = data_source['MAIN_DB2']['database']

    POOL = process_db2.db2pool(DB2_DICT, 5)  # 初始化数据库连接实例对象

    data = load_pre_data_excel()
    filter_data = filter_pre_data(data)  #只包含自动准备数据为是的行数据
    a = apd.analyze(filter_data)
    sql_str = format_sql(filter_data, 2, a, sql_path)
    print(sql_str)

    # cust_buy = db_pool.work(POOL, sql_str, 'S')
    # print(cust_buy)
