# -*- coding: utf-8 -*-

""" 用于整理通讯录
    包含：通讯录合并、去17951(86、+86)
"""

import shutil
import csv


class PhoneBook(object):
    """ 用于整理通讯录
        包含：通讯录合并、去17951(86、+86)
    """
    family_name = u'姓'.encode('gbk')
    radio_phone = u'无绳电话'.encode('gbk')
    mobile_phone = u'移动电话'.encode('gbk')
    phone_types = radio_phone, mobile_phone

    def __init__(self, input_file, output_file):
        self.__data = []
        self.__read_data(input_file)
        self.__write_data(output_file)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, per):
        self.__handle_phone_number(per)
        for each in self.__data:
            if self.__check_need_merge(each, per):
                self.__merge_phone_data(each, per)
                return
        self.__data.append(per)

    def __handle_phone_number(self, per):
        """ 去17951(86、+86) """
        if not per[self.radio_phone] and per[self.mobile_phone]:
            per[self.radio_phone] = per[self.mobile_phone]
            per[self.mobile_phone] = ''

        for phone in self.phone_types:
            for prefix in '17951', '+86', '86':
                if per[phone].startswith(prefix):
                    per[phone] = per[phone][len(prefix):]
                    break

    def __check_need_merge(self, each, per):
        if each[self.family_name] == per[self.family_name]:
            return True
        for phone in self.phone_types:
            if per[phone] \
                and per[phone] in [each[x] for x in self.phone_types]:
                    return True
        return False

    def __merge_phone_data(self, each, per):
        """ 合并通讯录 """
        for phone in self.phone_types:
            if per[phone] \
                and per[phone] not in [each[x] for x in self.phone_types]:
                    for x in self.phone_types:
                        if not each[x]:
                            each[x] = per[phone]
                            break

    def __get_fields(self, csvfile):
        with open(csvfile, 'rb') as rf:
            for row in csv.reader(rf):
                self.__fields = row
                break

    def __read_data(self, csvfile):
        self.__get_fields(csvfile)

        with open(csvfile, 'rb') as rf:
            reader = csv.DictReader(rf)
            for per in reader:
                self.data = per

    def __write_data(self, csvfile):
        with open(csvfile, 'wb') as wf:
            writer = csv.DictWriter(wf, fieldnames=self.__fields,
                    quoting=csv.QUOTE_ALL)
            writer.writeheader()

            for per in self.data:
                writer.writerow(per)


if __name__ == '__main__':
    phone_book = PhoneBook('tongxunlu.csv', 'tongxunlu.output.csv')
    shutil.copy('tongxunlu.output.csv', 'tongxunlu.output.txt')

