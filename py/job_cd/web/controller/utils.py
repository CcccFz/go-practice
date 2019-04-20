# -*- coding: utf-8 -*-

import re


def generate_mongodb_queryset(**kwargs):
    find_dict, sorted_list = {}, []
    if 'benefit_list' in kwargs and kwargs['benefit_list']:
        if '$and' not in find_dict:
            find_dict['$and'] = []
        find_dict['$and'].extend([{'benefit': re.compile(r'%s' % x)} for x in kwargs['benefit_list']])

    if 'salary_list' in kwargs and kwargs['salary_list']:
        salary_cond = []
        for salary in kwargs['salary_list']:
            if '-' in salary:
                min_v, max_v = [int(x[:-1]) for x in salary.split('-')]
            else:
                min_v, max_v = 26, 100
            salary_cond.append({'salary_min': {'$lte': max_v}, 'salary_max': {'$gte': min_v}})
        if salary_cond:
            if '$and' in find_dict:
                find_dict['$and'].append({'$or': salary_cond})
            else:
                find_dict['$or'] = salary_cond

    if 'sort_list' in kwargs and kwargs['sort_list']:
        for sort_by in kwargs['sort_list']:
            key = ''
            if '薪资' in sort_by:
                key = 'salary_max'
            elif '经验' in sort_by:
                key = 'experience_min'
            elif '规模' in sort_by:
                key = 'scale_max'
            else:
                key = 'actual_time'

            if 'down' in sort_by:
                sorted_list.append((key, -1))
            elif 'up' in sort_by:
                sorted_list.append((key, 1))
            else:
                pass

    return find_dict, sorted_list
