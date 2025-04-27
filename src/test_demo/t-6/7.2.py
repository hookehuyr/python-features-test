"""
Date: 2025-04-27 15:09:38
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-27 15:09:48
FilePath: /test-demo/src/test_demo/t-6/7.2.py
Description: 文件描述
"""

xs = {"a": 4, "c": 2, "b": 3, "d": 1}

for item in xs.items():
    print(item)

print(sorted(xs.items(), key=lambda x: x[1]))

import operator

print(sorted(xs.items(), key=operator.itemgetter(1)))
