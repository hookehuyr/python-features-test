"""
Date: 2025-04-26 20:24:40
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-26 20:25:05
FilePath: /test-demo/src/test_demo/t-5/3.3.py
Description: 文件描述
"""


class Car:

    def __init__(self, color, mileage, automatic):
        self.color = color
        self.mileage = mileage
        self.automatic = automatic

    def __repr__(self):
        return f"Car({self.color}, {self.mileage}, {self.automatic})"


car1 = Car("red", 3812.4, True)

print(car1)
