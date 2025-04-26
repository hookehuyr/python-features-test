"""
Date: 2025-04-26 23:04:22
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-26 23:04:49
FilePath: /test-demo/src/test_demo/t-5/5.3.py
Description: 文件描述
"""

from queue import LifoQueue

s = LifoQueue()
s.put("eat")
s.put("sleep")
s.put("code")

print(s)

print(s.get())
print(s.get())
print(s.get())

s.get_nowait()

s.get()
