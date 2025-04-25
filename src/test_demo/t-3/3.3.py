'''
Date: 2025-04-24 22:13:07
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-24 22:13:33
FilePath: /test-demo/src/test_demo/t-3/3.3.py
Description: 文件描述
'''


def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper


def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasis
def greet():
    return 'Hello!'

print(greet())
