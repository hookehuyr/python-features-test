"""
Date: 2025-04-26 01:04:09
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-26 01:06:31
FilePath: /test-demo/src/test_demo/t-4/8.6.py
Description: 文件描述
"""

import math


class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return f"Pizza({self.radius!r}, " f"{self.ingredients!r})"

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r**2 * math.pi

    pizza = Pizza(4, ["mozzarella", "tomatoes"])
    print(pizza)
    print(pizza.radius)
    print(pizza.ingredients)
    print(pizza.area())
    print(Pizza.circle_area(4))
