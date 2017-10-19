# 转义字符\:
print("I'm OK")
print('I\'m learning \n     Python\n')

# Python允许用r''表示''内部的字符串默认不转义
print('\\\t\\')
print(r'\\\t\\' '\n')

# Python允许用'''...'''的格式表示多行内容
print('''line1
line2
line3\n''')

# 布尔值(True/False)、与运算、或运算、条件判断
print(3 > 2)
print(-9 < -343)
print(True and True)
print(True and False)
print(True or False)
if 111 < 222:
    print('a')
else:
    print('b')
