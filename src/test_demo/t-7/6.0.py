"""
Date: 2025-04-27 16:52:55
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-27 16:53:03
FilePath: /test-demo/src/test_demo/t-7/6.0.py
Description: 文件描述
"""

mapping = {"a": 23, "b": 42, "c": 0xC0FFEE}
print(str(mapping))

import json
print(json.dumps(mapping, indent=4, sort_keys=True))

mapping['d'] = {1, 2, 3}

import pprint
pprint.pprint(mapping)
