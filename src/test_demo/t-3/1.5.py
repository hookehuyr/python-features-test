'''
Date: 2025-04-24 15:25:34
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-24 18:32:37
FilePath: /test-demo/src/test_demo/t-3/1.5.py
Description: 文件描述
'''


def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'

    def yell():
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper


# get_speak_func('Hello, World', 0.7)()


def make_adder(n):
    def adder(k):
        return k + n
    return adder


plus_3 = make_adder(3)
plus_5 = make_adder(5)
print(plus_3(4))
print(plus_5(4))

(lambda x: x + 3)(4)

sorted(range(-5, 6), key=lambda x: x * x)
# -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
