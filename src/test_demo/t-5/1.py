'''
Date: 2025-04-26 10:31:58
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-26 14:07:41
FilePath: /test-demo/src/test_demo/t-5/1.py
Description: 文件描述
'''
from collections import defaultdict
dd = defaultdict(list)

dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin')
dd['dogs'].append('Mr Sniffles')
# print(dd)

# s = 'abracadabra'
# char_count = defaultdict(int)
# for char in s:
#     char_count[char] += 1

# for char, count in char_count.items():
#     print(f'{char}: {count}')


# grouped_data = defaultdict(list)
# data = [(1, 'a'), (2, 'b'), (1, 'c')]
# for key, value in data:
#     grouped_data[key].append(value)

# print(grouped_data)  # Output: defaultdict(<class 'list'>, {1: ['a', 'c'], 2: ['b']})

# for key, values in grouped_data.items():
#     print(f'{key}: {values}')


# from collections import ChainMap
# dict1 = {'one': 1, 'two': 2}
# dict2 = {'three': 3, 'four': 4}
# chain_map = ChainMap(dict1, dict2)
# print(chain_map)


from types import MappingProxyType
writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)
print(read_only)
print(read_only['one'])
read_only['one'] = 23
print(read_only)
