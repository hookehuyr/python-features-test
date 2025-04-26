'''
Date: 2025-04-26 20:45:48
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-26 21:21:50
FilePath: /test-demo/src/test_demo/t-5/3.5.py
Description: 文件描述
'''
"""
Date: 2025-04-26 20:45:48
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-26 20:51:24
FilePath: /test-demo/src/test_demo/t-5/3.5.py
Description: 文件描述
"""

from typing import NamedTuple


class Car1(NamedTuple):
    color: str
    mileage: float
    automatic: bool

c = Car1('red', 1.1, True)

print(c)

from types import SimpleNamespace

c1 = SimpleNamespace(color='red', mileage=1.1, automatic=True)
print(c1.color)
