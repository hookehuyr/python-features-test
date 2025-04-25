'''
Date: 2025-04-25 16:06:09
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-25 16:25:33
FilePath: /test-demo/src/test_demo/t-4/4.3.py
Description: 文件描述
'''

import copy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"


class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return f'Rectangle({self.topleft!r}, ' f'{self.bottomright!r})'

rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)

print(rect)
