'''
Date: 2025-04-24 23:43:59
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-24 23:44:36
FilePath: /test-demo/src/test_demo/t-3/4.0.py
Description: 文件描述
'''


def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


foo('hello')
foo('hello', 1, 2, 3)
foo('hello', 1, 2, 3, key1='value', key2=999)

