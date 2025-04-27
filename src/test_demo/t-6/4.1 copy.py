'''
Date: 2025-04-27 13:31:10
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-27 14:33:04
FilePath: /test-demo/src/test_demo/t-6/4.1 copy.py
Description: 文件描述
'''


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)

class RepeaterIterator:
    def __init__(self, source):
        # source接收的就是Repeater类的实例
        self.source = source

    def __next__(self):
        # self.source 是对 Repeater 实例的引用，通过它可以访问 Repeater 实例的属性和方法
        # self.source.value 指的是 Repeater 实例所保存的值
        return self.source.value


# 使用示例：
repeater = Repeater("Hello")  # 创建一个重复器实例，重复值为"Hello"
for item in repeater:         # 使用for循环进行迭代
    print(item)              # 将无限打印"Hello"
    # 这里为了避免无限循环，我们只打印三次
    if next(repeater.__iter__()) == "Hello" * 3:
        break

# 方式二：手动调用迭代器
iterator = iter(repeater)
print(next(iterator))
print(next(iterator))
