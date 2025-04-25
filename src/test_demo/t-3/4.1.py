'''
Date: 2025-04-25 00:41:19
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-25 00:41:43
FilePath: /test-demo/src/test_demo/t-3/4.1.py
Description: 文件描述
'''


# def foo(x, *args, **kwargs):
#     kwargs['name'] = 'Alice'
#     new_args = args + ('extra', )
#     bar(x, *new_args, **kwargs)


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'


my_car = AlwaysBlueCar('red', 37281)
print(my_car.color)

