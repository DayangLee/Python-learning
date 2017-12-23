import math

# Python内置了很多有用的函数，可以直接调用
print(abs(100))  # 100
print(abs(-100))  # 100
print(max(1, 3, 5, -7))  # 5
print(int('123'))  # 123
print(float('12'))  # 12.0
print(str(1.23))  # 1.23
print(str(100))  # 100
print(bool(1))  # True
print(bool(''))  # False


# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-99))


# 空函数. 如果想定义一个什么事也不做的空函数，可以用pass语句：
# pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
    pass


print(nop())  # None


def my_grade(x):
    if x >= 90:
        return '优'
    elif x >= 80:
        return '良'
    elif x >= 70:
        pass
    else:
        return '不及格'


print(my_grade(50))  # 不及格
print(my_grade(77))  # None


# 参数检查
# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError：
# 但是如果参数类型不对，Python解释器就无法帮我们检查
# 当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善。
# 修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
# 添加了参数检查后，如果传入错误的参数类型，函数就可以抛出一个错误：
def my_abs1(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type ~~~')
    if x >= 0:
        return x
    else:
        return -x


# abs('1')  # TypeError: bad operand type for abs(): 'str'
# my_abs('1')  # TypeError: unorderable types: str() >= int()
# my_abs1('h')  # TypeError: bad operand type ~~~

# 返回多个值
# 页面顶部import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)  # 151.96152422706632 130.0
r = move(100, 100, 60, math.pi / 6)
print(r)  # (151.96152422706632, 130.0)

# 其实返回值仍是单一直，它是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

# 函数的参数
# Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(3, 3))  # 27

# 默认参数


def power1(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power1(5))  # 25
print(power1(5, 3))  # 125

# 默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错
# 二是如何设置默认参数
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数
# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。

