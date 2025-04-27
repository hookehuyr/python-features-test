"""
Date: 2025-04-27 15:50:26
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-27 16:11:46
FilePath: /test-demo/src/test_demo/t-7/3.0.py
Description: 文件描述
"""


def dispatch_if(operator, x, y):
    if operator == "add":
        return x + y
    elif operator == "sub":
        return x - y
    elif operator == "mul":
        return x * y
    elif operator == "div":
        return x / y
    else:
        return None

import operator

# 定义全局操作字典
opt_dict = {
    "add": operator.add,
    "sub": operator.sub,
    "mul": operator.mul,
    "div": operator.truediv,
}

def dispatch_dict(operator: str, x: float, y: float) -> float:
    """使用字典分发方式进行数学运算

    Args:
        operator: 运算符，可选值为'add'、'sub'、'mul'、'div'
        x: 第一个操作数
        y: 第二个操作数

    Returns:
        运算结果，如果运算符不支持则返回None
    """
    func = opt_dict.get(operator)
    if func is not None:
        return func(x, y)
    else:
        return None

print(dispatch_dict("add", 1, 2))
