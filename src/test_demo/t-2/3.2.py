'''
Date: 2025-04-23 15:51:07
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-23 15:57:48
FilePath: /test-demo/src/test_demo/t-2/3.2.py
Description: 基于上下文管理器和装饰器的两种方式实现缩进打印器
'''

'''
实现一：使用类实现的上下文管理器
- 通过定义__enter__和__exit__方法实现上下文管理
- 每次进入上下文时增加缩进级别
- 每次退出上下文时减少缩进级别
- 提供print方法实现带缩进的文本打印
'''

# 实现一：基于类的上下文管理器

class Indenter:
    def __init__(self):
        # 初始化缩进级别为0
        self.level = 0

    def __enter__(self):
        # 进入上下文时，缩进级别加1
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # 退出上下文时，缩进级别减1
        self.level -= 1

    def print(self, text):
        # 根据当前缩进级别打印文本
        # 每个缩进级别用4个空格表示
        print('    ' * self.level + text)


# 测试类实现的缩进打印器
with Indenter() as indent:
    indent.print('hi!')  # 缩进级别1
    with indent:
        indent.print('hello')  # 缩进级别2
        with indent:
            indent.print('bonjour')  # 缩进级别3
    indent.print('hey')  # 缩进级别1


# 实现二：使用装饰器实现的上下文管理器
from contextlib import contextmanager

@contextmanager
def indenter():
    # 在上下文外部维护缩进级别
    level = [0]

    try:
        # 进入上下文时增加缩进级别
        level[0] += 1
        # 定义内部打印函数

        def print_indented(text):
            print('    ' * level[0] + text)
        # 返回打印函数供上下文内使用
        yield print_indented
    finally:
        # 退出上下文时减少缩进级别
        level[0] -= 1


# 测试装饰器实现的缩进打印器
with indenter() as print_l1:
    print_l1('hi!')  # 缩进级别1
    with indenter() as print_l2:
        print_l2('hello')  # 缩进级别2
        with indenter() as print_l3:
            print_l3('bonjour')  # 缩进级别3
    print_l1('hey')  # 缩进级别1
