# coding:utf-8

import yaml

data_source = {}
detail = {}
business_source = {}


class PyrunConfig:
    def __init__(self, filename):
        self.filename = filename
        self.path = r'F:\11-开发项目\pyrun_rebuild\pyrun_rebuild\cfg' + '\\' + self.filename

    def read_app_config(self):
        with open(self.path, mode='r+') as f:
            config = yaml.full_load(f)
        global data_source
        data_source = config['DATA_SOURCE']
        global detail
        detail = config['DETAIL']

        return data_source, detail

    def read_business_config(self):
        with open(self.path, mode='r+') as f:
            config = yaml.full_load(f)
        global business_source
        business_source = config['business']

        return business_source


if __name__ == '__main__':
    app_cfg = PyrunConfig('app_config.yml')
    business_cfg = PyrunConfig('business_config.yml')
    data_source, detail = app_cfg.read_app_config()
    business = business_cfg.read_business_config()
    print(data_source)
