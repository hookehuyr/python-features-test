# Python闭包学习教程

## 一、闭包的定义
在Python中，闭包是一种特殊的函数对象，它允许一个函数记住并访问其定义时所在的外部作用域的变量，即使在该外部函数已经返回之后。闭包由两部分组成：内部函数和该内部函数能够访问的外部函数作用域中的变量。

## 二、闭包的构成条件
1. **内部函数定义在外部函数内部**：内部函数必须在外部函数的作用域内定义。
2. **内部函数使用外部函数的变量**：内部函数使用了外部函数作用域中的变量。
3. **外部函数返回内部函数**：外部函数返回内部函数对象，而不是直接调用内部函数。

## 三、简单示例
```python
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function


closure = outer_function(10)
result = closure(5)
print(result)  # 输出 15
```
在这个例子中：
 - `outer_function`是外部函数，它接受一个参数`x`。
 - `inner_function`是内部函数，它定义在`outer_function`内部，并且使用了外部函数的变量`x`。
 - `outer_function`返回`inner_function`函数对象。
 - `closure`是通过调用`outer_function(10)`得到的闭包。当调用`closure(5)`时，实际上是调用了`inner_function`，并且`inner_function`可以访问并使用在其定义时外部函数`outer_function`作用域中的变量`x`（此时`x`的值为10）。

## 四、闭包的作用
1. **数据隐藏与封装**：闭包可以将一些数据（外部函数的变量）与操作这些数据的函数封装在一起，外部代码只能通过闭包函数来间接访问和修改这些数据，从而实现数据隐藏和保护。
```python
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner


my_counter = counter()
print(my_counter())  # 输出 1
print(my_counter())  # 输出 2
```
在这个计数器示例中，`count`变量被封装在闭包内部，外部代码无法直接访问和修改`count`，只能通过调用闭包函数`my_counter`来增加`count`的值。

2. **创建可定制的函数**：通过在外部函数传入不同的参数，可以创建具有不同行为的闭包函数。
```python
def multiplier(factor):
    def multiply_by_factor(number):
        return number * factor
    return multiply_by_factor


multiply_by_two = multiplier(2)
multiply_by_three = multiplier(3)

print(multiply_by_two(5))  # 输出 10
print(multiply_by_three(5))  # 输出 15
```
这里通过`multiplier`函数传入不同的`factor`值，创建了两个不同行为的闭包函数`multiply_by_two`和`multiply_by_three`。

## 五、闭包与变量作用域
1. **注意变量的生命周期**：闭包中的外部变量在外部函数返回后仍然存在，因为内部函数对其有引用。但是，如果外部函数重新调用，会创建新的外部作用域和新的变量。
```python
def outer():
    num = 10
    def inner():
        nonlocal num
        num += 1
        return num
    return inner


func1 = outer()
func2 = outer()

print(func1())  # 输出 11
print(func2())  # 输出 11，因为func2有自己独立的num变量
```
2. **`nonlocal`关键字**：当内部函数需要修改外部函数作用域中的变量时，如果该变量是不可变类型（如整数、字符串），需要使用`nonlocal`关键字声明。如果不使用`nonlocal`，Python会认为在内部函数中创建了一个新的局部变量。
```python
def outer():
    value = 10
    def inner():
        value = 20  # 这里会创建一个新的局部变量value，而不是修改外部的value
        return value
    result = inner()
    return result, value


result, value = outer()
print(result)  # 输出 20
print(value)  # 输出 10
```
使用`nonlocal`关键字：
```python
def outer():
