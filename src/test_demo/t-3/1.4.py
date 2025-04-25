'''
Date: 2025-04-24 02:33:07
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-24 15:06:59
FilePath: /test-demo/src/test_demo/t-3/1.4.py
Description: 文件描述
'''


def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)


# print(speak('Hello, World'))


def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'

    def yell(text):
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper

get_speak_func(0.3)
