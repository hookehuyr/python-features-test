"""
Date: 2025-04-25 21:07:10
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-25 21:08:48
FilePath: /test-demo/src/test_demo/t-4/7.1.py
Description: 文件描述
"""


class CountedObject:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1


print(CountedObject.num_instances)
CountedObject()
print(CountedObject.num_instances)
CountedObject()
print(CountedObject.num_instances)
CountedObject()
print(CountedObject.num_instances)


class BuggyCountedObject:
    num_instances = 0

    def __init__(self):
        self.num_instances += 1

print()

print(BuggyCountedObject.num_instances)
print(BuggyCountedObject().num_instances)
print(BuggyCountedObject().num_instances)
print(BuggyCountedObject().num_instances)
print(BuggyCountedObject.num_instances)
