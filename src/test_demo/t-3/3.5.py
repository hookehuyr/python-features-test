'''
Date: 2025-04-24 23:20:25
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-24 23:27:06
FilePath: /test-demo/src/test_demo/t-3/3.5.py
Description: 文件描述
'''
import functools

def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


def greet():
    """Return a friendly greeting."""
    return 'Hello!'


decorated_greet = uppercase(greet)
print(greet.__name__)
print(greet.__doc__)

print(decorated_greet.__name__)
print(decorated_greet.__doc__)
