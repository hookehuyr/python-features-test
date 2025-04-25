'''
Date: 2025-04-23 18:07:41
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-23 23:29:48
FilePath: /test-demo/src/test_demo/t-2/4.3.py
Description: 文件描述
'''
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 42

# t = Test()
# print(dir(t))


class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'

t2 = ExtendedTest()
print(t2.foo)
print(t2._bar)
print(t2.__baz)

# list()
# _.append(1)
# print(_)
