'''
Date: 2025-04-24 01:54:38
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-24 02:32:10
FilePath: /test-demo/src/test_demo/t-3/1.1.py
Description: 文件描述
'''


def bark(str):
    return str.upper()
def bark_more(str, count):
    return str.upper() + '<>' + count

def whisper(str):
    return str.lower() + '...'


def greet(func):
    greeting = func('Hi, I am a python program!')
    print(greeting)


# greet(bark)
# greet(whisper)

# list(map(bark, ['hello', 'heyho', 'good morning']))
result = list(map(bark_more, ['hello', 'heyho', 'good morning'], ['1', '2', '3']))
print(result)
