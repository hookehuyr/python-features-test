'''
Date: 2025-04-24 22:24:04
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-24 22:52:09
FilePath: /test-demo/src/test_demo/t-3/3.4.py
Description: 文件描述
'''


# def proxy(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result
#     return wrapper


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() with {args}, {kwargs}')

        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() returned {original_result!r}')
        return original_result
    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


say('Jane', 'Hello, World')
