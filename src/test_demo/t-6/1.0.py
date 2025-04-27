'''
Date: 2025-04-26 23:54:12
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-27 00:01:40
FilePath: /test-demo/src/test_demo/t-6/1.0.py
Description: 文件描述
'''

my_items = ['a', 'b', 'c']

i = 0
while i < len(my_items):
    print(my_items[i])
    i += 1

for item in my_items:
    print(item)

for i, item in enumerate(my_items):
    print(f'{i}: {item}')
