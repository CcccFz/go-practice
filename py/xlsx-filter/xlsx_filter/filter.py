# -*- coding: utf-8 -*-
__author__ = 'Duome'


""" 运算方法总和的类
    过滤价格Remove
"""

class Filter(object):

    def __init__(self, src_data):
        self.src_data = src_data
        self.result_data = {}
        self.rules = []


    def get_result(self):
        for sheetname, sheet_data in self.src_data.items():
            self.result_data[sheetname] = []
            self.result_data[sheetname].append(sheet_data[0])

            for row in range(1, len(sheet_data)):
                for check_rule in self.rules:
                    if check_rule(sheet_data[row]):
                        self.result_data[sheetname].append(sheet_data[row])

        return self.result_data
