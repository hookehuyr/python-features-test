`collections.defaultdict` 是 Python 标准库 `collections` 模块中的一个类，它是 `dict` 的子类，提供了一种在字典中设置默认值的便捷方式。以下通过示例详细说明它的功能：

### 1. 基本使用

通常，当你尝试访问字典中不存在的键时，会引发 `KeyError`。而 `defaultdict` 会在访问不存在的键时，自动使用你提供的默认值工厂函数创建一个默认值。

```python
from collections import defaultdict

# 创建一个 defaultdict，默认值工厂函数为 int，int() 返回 0
d = defaultdict(int)
print(d['a'])  # 访问不存在的键 'a'，会自动创建默认值 0
```

在上述代码中，我们创建了一个 `defaultdict`，其默认值工厂函数是 `int`。当访问不存在的键 `'a'` 时，`defaultdict` 会自动调用 `int()` 生成默认值 `0` 并返回，同时将 `'a': 0` 这个键值对添加到字典中。

### 2. 常见用途 - 计数

`defaultdict(int)` 常用于计数场景。例如，统计字符串中每个字符出现的次数：

```python
from collections import defaultdict

s = 'abracadabra'
char_count = defaultdict(int)
for char in s:
    char_count[char] += 1

for char, count in char_count.items():
    print(f'{char}: {count}')
```

这里，每次遇到一个字符，我们直接对其计数加一。即使该字符是第一次出现（字典中不存在该键），`defaultdict` 也会自动提供默认值 `0`，确保计数操作顺利进行。

### 3. 自定义默认值工厂函数

默认值工厂函数可以是任何可调用对象，不一定是内置类型。例如，如果你想让不存在的键默认对应一个空列表，可以这样做：

```python
from collections import defaultdict

grouped_data = defaultdict(list)
data = [(1, 'a'), (2, 'b'), (1, 'c')]
for key, value in data:
    grouped_data[key].append(value)

for key, values in grouped_data.items():
    print(f'{key}: {values}')
```

在这个例子中，`defaultdict(list)` 确保当访问一个不存在的键时，会自动创建一个空列表。这样，我们可以方便地将具有相同键的数据分组到对应的列表中。

### 4. 与普通字典的对比

普通字典在访问不存在的键时需要繁琐的检查和初始化步骤：

```python
regular_dict = {}
data = [(1, 'a'), (2, 'b'), (1, 'c')]
for key, value in data:
    if key not in regular_dict:
        regular_dict[key] = []
    regular_dict[key].append(value)

for key, values in regular_dict.items():
    print(f'{key}: {values}')
```



相比之下，`defaultdict` 简化了代码，使逻辑更清晰，减少了处理不存在键时的样板代码。