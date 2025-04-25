"""
Date: 2025-04-25 17:37:51
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-25 17:45:04
FilePath: /test-demo/src/test_demo/t-4/6.1.py
Description: 文件描述
"""

from collections import namedtuple
import json

Car = namedtuple("Car2", "color mileage")

my_car = Car("red", 3812.4)
# print(my_car.color)
# print(my_car.mileage)
# print(my_car[0])

# print(*my_car)
print(json.dumps(my_car._asdict()))
