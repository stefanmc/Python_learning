# coding:utf-8

import yaml

data_source = {}
detail = {}

class PyrunConfig:
    def __init__(self):
        with open(r'F:\11-开发项目\pyrun_rebuild\pyrun_rebuild\cfg\config.yml', mode='r+') as f:
            config = yaml.full_load(f)
        global data_source
        data_source = config['DATA_SOURCE']
        global detail
        detail = config['DETAIL']


if __name__ == '__main__':
    PyrunConfig()
    print(data_source)
    print(detail)
