'''
Date: 2025-04-24 21:52:36
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-24 23:23:09
FilePath: /test-demo/src/test_demo/t-3/3.2.py
Description: 文件描述
'''


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


@uppercase
def say_hi():
    return 'hello there'

print(say_hi())
