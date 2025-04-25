'''
Date: 2025-04-25 09:56:26
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-25 14:33:35
FilePath: /test-demo/src/test_demo/t-4/2.0.py
Description: 文件描述
'''


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return 'a {a.color} car'.format(a=self)


my_car = Car('red', 3721.4)
print(my_car)
my_car
