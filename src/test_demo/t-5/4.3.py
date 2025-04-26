'''
Date: 2025-04-26 22:09:40
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-26 22:18:37
FilePath: /test-demo/src/test_demo/t-5/4.3.py
Description: 文件描述
'''

# from collections import Counter

# inventory = Counter()
# loot = {"sword": 1, "bread": 3}
# inventory.update(loot)
# print(inventory)

# more_loot = {'sword': 1, 'apple': 1}
# inventory.update(more_loot)
# print(inventory)


from collections import Counter
text = "hello world hello python"
print(text.split())
word_count = Counter(text.split())
print(word_count)
