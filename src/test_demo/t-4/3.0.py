'''
Date: 2025-04-25 15:02:20
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-25 16:23:03
FilePath: /test-demo/src/test_demo/t-4/3.0.py
Description: 文件描述
'''

# class NameTooShortError(ValueError):
#     pass


class BaseValidationError(ValueError):
    pass


class NameTooShortError(BaseValidationError):
    pass


class NameTooLongError(BaseValidationError):
    pass


class NameTooCuteError(BaseValidationError):
    pass


def validate(name):
    """
    验证输入名称的有效性

    参数:
        name: 要验证的名称字符串

    抛出:
        NameTooShortError: 当名称长度小于3时
        NameTooLongError: 当名称长度大于10时
        NameTooCuteError: 当名称包含'可爱'时
    """
    if len(name) < 3:
        raise NameTooShortError(f'名称"{name}"太短，至少需要3个字符')
    if len(name) > 10:
        raise NameTooLongError(f'名称"{name}"太长，最多允许10个字符')
    if "可爱" in name:
        raise NameTooCuteError(f'名称"{name}"太可爱了')


def handle_validation_error(err):
    """
    处理验证错误

    参数:
        err: 捕获的验证错误异常
    """
    print(f"验证错误: {err}")


try:
    validate("a")
except BaseValidationError as err:
    handle_validation_error(err)
