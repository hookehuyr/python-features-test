"""
Date: 2025-04-26 17:38:55
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-26 17:40:58
FilePath: /test-demo/src/test_demo/t-5/2.4.py
Description: 文件描述
"""

arr = "abcd"
# 字符串可以解包到列表中，从而得到可变版本：
arr = list(arr)
# 然后就可以用列表的方法了
arr.append("e")
arr.insert(0, "x")
arr.remove("c")
arr.pop()
arr.reverse()
arr.sort()
# 最后再把列表还原成字符串：
arr = "".join(arr)
print(arr)
