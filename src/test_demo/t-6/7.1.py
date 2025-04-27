'''
Date: 2025-04-27 14:46:39
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-27 14:51:02
FilePath: /test-demo/src/test_demo/t-6/7.1.py
Description: 文件描述
'''

name_for_userid = {
    382: 'Alice',
    950: 'Bob',
    590: 'Dilbert',
}

def greeting(userid):
    return 'Hi %s!' % name_for_userid.get(userid, 'there')
print(greeting(382))
print(greeting(33333333))
