'''
Date: 2025-04-23 14:09:04
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-23 14:44:50
FilePath: /test-demo/src/test_demo/t-2/1.py
Description: 文件描述
'''


def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price


shoes = {'name': 'Fancy Shoes', 'price': 14900}
print(apply_discount(shoes, 0.25))
print(apply_discount(shoes, 2.0))
