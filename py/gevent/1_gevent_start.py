# coding: utf-8

import gevent


def foo():
    print 'Runing in foo...'
    gevent.sleep(0)
    print 'Context switch back to run in foo...'

def bar():
    print 'Context switch to run in bar...'
    gevent.sleep(0)
    print 'Context again switch to run in bar...'

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
    ])

