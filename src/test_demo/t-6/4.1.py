"""
Date: 2025-04-27 11:46:41
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-27 13:05:56
FilePath: /test-demo/src/test_demo/t-6/4.1.py
Description: 文件描述
"""


class Repeater:
    """无限迭代器类

    这个类实现了一个无限迭代器，可以无限次重复返回初始化时传入的值。
    通过实现__iter__方法使得类的实例可以在for循环中使用。

    Attributes:
        value: 要重复的值，可以是任意类型
    """

    def __init__(self, value):
        """初始化Repeater实例

        Args:
            value: 要重复的值，可以是任意类型
        """
        self.value = value

    def __iter__(self):
        """返回一个迭代器对象

        实现了__iter__方法使得类的实例可以在for循环中使用。
        每次调用都会返回一个新的RepeaterIterator实例。

        Returns:
            RepeaterIterator: 一个新的迭代器实例
        """
        return RepeaterIterator(self)


class RepeaterIterator:
    """迭代器实现类

    这个类实现了实际的迭代器功能，通过__next__方法返回源Repeater实例中存储的值。
    由于没有停止条件，这是一个无限迭代器。

    Attributes:
        source: Repeater实例的引用
    """

    def __init__(self, source):
        """初始化RepeaterIterator实例

        Args:
            source: Repeater实例的引用，用于获取要重复的值
        """
        self.source = source

    def __next__(self):
        """返回下一个值

        每次调用都返回源Repeater实例中存储的值。
        由于没有停止条件，这个方法会无限次返回相同的值。

        Returns:
            任意类型: 源Repeater实例中存储的值
        """
        return self.source.value


# 使用示例：
# repeater = Repeater("Hello")  # 创建一个重复器实例，重复值为"Hello"
# for item in repeater:         # 使用for循环进行迭代
#     print(item)              # 将无限打印"Hello"
