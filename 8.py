import math


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
