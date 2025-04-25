"""
Date: 2025-04-25 23:35:10
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-25 23:36:35
FilePath: /test-demo/src/test_demo/t-4/8.0.py
Description: 文件描述
"""


class MyClass:
    def method(self):
        return "instance method called", self

    @classmethod
    def classmethod(cls):
        return "class method called", cls

    @staticmethod
    def staticmethod():
        return "static method called"


# obj = MyClass()
# print(obj.method())
# print(MyClass.method(obj))

# print(obj.classmethod())
# print(MyClass.classmethod())

# print(obj.staticmethod())


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    def __repr__(self):
        return f"Pizza({self.ingredients!r})"

Pizza(['cheese', 'tomatoes'])
