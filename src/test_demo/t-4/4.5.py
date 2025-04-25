"""
Date: 2025-04-25 16:40:30
LastEditors: hookehuyr hookehuyr@gmail.com
LastEditTime: 2025-04-25 17:02:51
FilePath: /test-demo/src/test_demo/t-4/4.5.py
Description: 文件描述
"""

"""
    无法实例化基类
    如果忘记在其中一个子类中实现接口方法，那么要尽早报错
"""

from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Concrete(Base):
    def foo(self):
        pass

    # 又忘记声明 bar()了……
    # def bar(self):
    #     pass


b = Base()
# b.foo()

# c = Concrete()
# c.foo()
# c.bar()

assert issubclass(Concrete, Base)
