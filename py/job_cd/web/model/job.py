# -*- coding: utf-8 -*-


from web import mongo


class Job(object):
    col = 'lagou'

    @classmethod
    def find(cls, find_dict, sort_list):
        if sort_list:
            return mongo.db[cls.col].find(find_dict, {'_id': 0}).sort(sort_list)
        else:
            return mongo.db[cls.col].find(find_dict, {'_id': 0})
