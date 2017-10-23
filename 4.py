# list
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['jy', 'dayang', 'junyanglee']
print(classmates)
print(len(classmates))  # 3
print(classmates[1])  # dayang
print(classmates[len(classmates) - 1])  # junyanglee
print(classmates[-1])  # junyanglee
print(classmates[-3])  # jy

# list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('Jay')
print(classmates)  # ['jy', 'dayang', 'junyanglee', 'Jay']

# 也可以把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(1, 'Jack')
print(classmates)  # ['jy', 'Jack', 'dayang', 'junyanglee', 'Jay']

# 要删除list的元素，用pop()方法：
classmates.pop()
print(classmates)  # ['jy', 'Jack', 'dayang', 'junyanglee']
classmates.pop(1)
print(classmates)  # ['jy', 'dayang', 'junyanglee']

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[2] = 'dayangLee'
print(classmates)  # ['jy', 'dayang', 'dayangLee']

# list里面的元素的数据类型也可以不同, list元素也可以是另一个list
item1 = ['Apple', 123, True]
item2 = ['Python', 'Java', ['Vue', 'React'], 'Ruby']
print(item2[2][1])  # 'React'

# tuple
# Python中另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
names = ('Michael', 'Bob', 'Tracy')
# 现在，names这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用names[0]，names[-1]，但不能赋值成另外的元素。
# 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
t1 = (1, 2)
print(t1)  # (1,2)
t2 = ()
print(t2)  # ()
t3 = (1)
print(t3)  # 1
# 注意，定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
# 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t4 = (1, )
print(t4)  # (1,)

# tuple不可变！！！
t5 = ('a', 'b', ['A', 'B'])
t5[2][0] = 'X'
t5[2][1] = 'Y'
print(t5)  # ('a', 'b', ['X', 'Y'])
# 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
# 理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变
