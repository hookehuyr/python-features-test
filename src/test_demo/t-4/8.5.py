"""
Date: 2025-04-25 23:57:42
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-26 00:46:28
FilePath: /test-demo/src/test_demo/t-4/8.5.py
Description: 文件描述
"""


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f"Pizza({self.ingredients!r})"

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomatoes"])

    @classmethod
    def prosciutto(cls):
        return cls(["mozzarella", "tomatoes", "ham"])
