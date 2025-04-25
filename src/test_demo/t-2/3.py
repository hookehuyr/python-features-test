'''
Date: 2025-04-23 15:14:49
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-23 15:31:23
FilePath: /test-demo/src/test_demo/t-2/3.py
Description: 文件描述
'''


# class ManageFile:
#     def __init__(self, name):
#         self.name = name

#     def __enter__(self):
#         self.file = open(self.name, 'w')
#         return self.file

#     def __exit__(self, exc_type, exc_value, traceback):
#         if self.file:
#             self.file.close()

# with ManageFile('hello.txt') as f:
#     f.write('hello, world!')
#     f.write('bye now')

from contextlib import contextmanager

'''
代码执行流程
    - 进入 with 语句块：当执行 with manage_file('hello.txt') as f: 时，manage_file 函数开始执行。
    - try 块中的操作：在 try 块里，f = open(name, 'w') 打开文件并将文件对象赋值给 f。
    - yield 语句：yield f 语句暂停函数的执行，并将文件对象 f 作为 with 语句中 as 后面变量的值返回。
    此时，控制权转移到 with 语句块内部，执行 f.write('hello, world!') 和 f.write('bye now') 等操作。
    - 离开 with 语句块：当 with 语句块执行完毕（无论是正常结束还是因为异常退出），控制权会回到 manage_file 函数中 yield 语句的下一行。
    - finally 块中的操作：finally 块中的 f.close() 会被执行，确保文件被关闭。

    通过这种方式，yield 起到了分割执行流程的作用，使得在 yield 之前的代码作为上下文管理器的 __enter__ 方法执行，在 yield 之后的代码作为上下文管理器的 __exit__ 方法执行。

'''

@contextmanager
def manage_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()


with manage_file('hello.txt') as f:
    f.write('hello, world!')
    f.write('bye now')
