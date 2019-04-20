# -*- coding: utf-8 -*-

import sys
import thulac
from collections import Counter

thu_handler = thulac.thulac()
cut = thu_handler.fast_cut
cut_f = thu_handler.fast_cut_f

DICT = {
    'n': '名词',
    'np': '人名',
    'ns': '地名',
    'ni': '机构名',
    'nz': '其它专名',
    'm': '数词',
    'q': '量词',
    'mq': '数量词',
    't': '时间词',
    'f': '方位词',
    's': '处所词',
    'v': '动词',
    'a': '形容词',
    'd': '副词',
    'h': '前接成分',
    'k': '后接成分',
    'i': '习语',
    'j': '简称',
    'r': '代词',
    'c': '连词',
    'p': '介词',
    'u': '助词',
    'y': '语气助词',
    'e': '叹词',
    'o': '拟声词',
    'g': '语素',
    'w': '标点',
    'x': '其它'
}


if __name__ == '__main__':
    db, texts = [], []
    with open('input.txt', 'rb') as rf:
        db = set(map(lambda x: x[0].strip(), cut(rf.read())))
    # with open('input.txt', 'rb') as rf:
    #     for (word, tag), cnt in Counter(map(lambda x: tuple(x), cut(rf.read()))).iteritems():
    #         texts.append('%s %s %d' % (word.strip(), tag, cnt))

    with open(sys.argv[1], 'rb') as rf:
        for (word, tag), cnt in Counter(map(lambda x: tuple(x), cut(rf.read()))).iteritems():
            w = word.strip()
            v = '小学词汇' if w in db else '可能是非小学词汇'
            tag = DICT[tag.strip()] if tag in DICT else '其它'
            s = '%s  %s  %d  %s' % (w, tag, cnt, v)
            print s
            texts.append(s)

    with open('output.txt', 'w') as wf:
        wf.write('\n'.join(texts))
