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
# 默认参数必须指向不变对象！！！


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


print(enroll('Dayang', 'F'))
print(enroll('JY', 'M', 24, 'Xi\'an'))


# 可变参数
# 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
# 要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))  # 14


# 改为可变参数，定义为下
def calc1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc1(1, 2, 3))  # 14
nums = [1, 2, 3]
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
print(calc1(*nums))  # 14

# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
# 函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数, 也可以传入任意个数的关键字参数
# 关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Dayang', 24)  # name: Dayang age: 24 other: {}
person(
    'JY', 23, city='Beijing', Job="nngineer"
)  # name: JY age: 23 other: {'Job': 'nngineer', 'city': 'Beijing'}
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra
       )  # name: Jack age: 24 other: {'job': 'Engineer', 'city': 'Beijing'}

# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
# 仍以person()函数为例，我们希望检查是否有city和job参数：


def person1(name, age, **kw):
    if 'city' in kw:
        return
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person1(
    'Jack1', 24, addr='Chaoyang', zipcode=123456
)  # name: Jack1 age: 24 other: {'zipcode': 123456, 'addr': 'Chaoyang'}
person1('Jack2', 24, city='Beijing', addr='Chaoyang', zipcode=123456)  #


# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person2(name, age, *, city, job):
    print(name, age, city, job)


# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# 调用方式如下：
person2('Jack', 24, city='Beijing', job='Engineer')  # Jack 24 Beijing Engineer


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person3(name, age, *args, city, job):
    print(name, age, args, city, job)


# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
person3(
    'Jack', 24, 'haha', city='Beijing',
    job='Engineer')  # Jack 24 ('haha',) Beijing Engineer


# 命名关键字参数可以有缺省值，从而简化调用：
def person4(name, age, *, city='Beijing', job):
    print(name, age, city, job)


# 由于命名关键字参数city具有默认值，调用时，可不传入city参数：
person4('Jack', 24, job='Engineer')  # Jack 24 Beijing Engineer


# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 比如定义一个函数，包含上述若干种参数：
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
