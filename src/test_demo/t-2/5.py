'''
Date: 2025-04-24 00:17:21
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-24 01:19:36
FilePath: /test-demo/src/test_demo/t-2/5.py
Description: 文件描述
'''

errno = 50159747054
name = 'Bob'

# print('Hello, %s' % name)
# print('%x' % errno)
# print('Hey %s, there is a 0x%x error!' % (name, errno))
# print('Hey %(name)s, there is a 0x%(errno)x error!)') % { "name": name, "errno": errno }

# from string import Template
# # 定义模板字符串，使用$符号表示变量
# templ_string = 'Hey $name, there is a $error error!'
# Template(templ_string).substitute(name=name, error=hex(errno))

SECRET = 'this-is-a-secret'
class Error:
    def __init__(self):
        pass
err = Error()
user_input = '{error.__init__.__globals__[SECRET]}'
# 安全性问题在于那个字符串可以访问到属性了
print(user_input.format(error=err))
