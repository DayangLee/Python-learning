# 字符串和编码
# 字符编码笔记：ASCII，Unicode和UTF-8(阮一峰)(http://www.ruanyifeng.com/blog/2007/10/ascii_unicode_and_utf-8.html)
# 字符串也是一种数据类型，但是，字符串比较特殊的是还有一个编码问题。
# 因为计算机只能处理数字，如果要处理文本，就必须先把文本转换为数字才能处理。最早的计算机在设计时采用8个比特（bit）作为一个字节（byte），所以，一个字节能表示的最大的整数就是255（二进制11111111=十进制255），如果要表示更大的整数，就必须用更多的字节。比如两个字节可以表示的最大整数是65535，4个字节可以表示的最大整数是4294967295。
# 由于计算机是美国人发明的，因此，最早只有127个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为ASCII编码，比如大写字母A的编码是65，小写字母z的编码是122。
# 但是要处理中文显然一个字节是不够的，至少需要两个字节，而且还不能和ASCII编码冲突，所以，中国制定了GB2312编码，用来把中文编进去。
# 你可以想得到的是，全世界有上百种语言，日本把日文编到Shift_JIS里，韩国把韩文编到Euc-kr里，各国有各国的标准，就会不可避免地出现冲突，结果就是，在多语言混合的文本中，显示出来会有乱码。
# 因此，Unicode应运而生。Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了。
# Unicode标准也在不断发展，但最常用的是用两个字节表示一个字符（如果要用到非常偏僻的字符，就需要4个字节）。现代操作系统和大多数编程语言都直接支持Unicode。
# 现在，捋一捋ASCII编码和Unicode编码的区别：ASCII编码是1个字节，而Unicode编码通常是2个字节。
# 字母A用ASCII编码是十进制的65，二进制的01000001；
# 字符0用ASCII编码是十进制的48，二进制的00110000，注意字符'0'和整数0是不同的；
# 汉字中已经超出了ASCII编码的范围，用Unicode编码是十进制的20013，二进制的01001110 00101101。
# 你可以猜测，如果把ASCII编码的A用Unicode编码，只需要在前面补0就可以，因此，A的Unicode编码是00000000 01000001。
# 新的问题又出现了：如果统一成Unicode编码，乱码问题从此消失了。但是，如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。
# 所以，本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间：

#  字符	   ASCII	        Unicode	          UTF-8
#   A    01000001    00000000 01000001    01000001
#   中      x        01001110 00101101    11100100 101110000 10101101

# 从上面的表格还可以发现，UTF-8编码有一个额外的好处，就是ASCII编码实际上可以被看成是UTF-8编码的一部分，所以，大量只支持ASCII编码的历史遗留软件可以在UTF-8编码下继续工作。

# 搞清楚了ASCII、Unicode和UTF-8的关系，我们就可以总结一下现在计算机系统通用的字符编码工作方式：

# 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

# 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件

# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
print('你好')
print('劉邦')
print('僕が死のうと思ったのは')
print('привет')

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示(字符=>Unicode)，chr()函数把编码转换为对应的字符(Unicode=>字符)：
print(ord('A'))  # 65
print(ord('中'))  # 20013
print(chr(66))  # B
print(chr(25991))  # 文

# 如果知道字符的整数编码，还可以用十六进制这么写str：
print('\u4e2d\u6587')

# 两种写法完全是等价的。
# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes(字符=>指定编码)，例如：
print('ABC'.encode('ascii'))  # b'ABC'
print('中文'.encode('utf-8'))  # b'\xe4\xb8\xad\xe6\x96\x87'
# print('中文'.encode('ascii'))  # UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
# 在bytes中，无法显示为ASCII字符的字节，用\x##显示。
# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法(指定编码=>字符)：
print(b'ABC'.decode('ascii'))  # ABC
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 中文

# 要计算str包含多少个字符，可以用len()函数：
print(len('ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

# 格式化

# 最后一个常见的问题是如何输出格式化的字符串。我们经常会输出类似'亲爱的xxx你好！你xx月的话费是xx，余额是xx'之类的字符串，而xxx的内容都是根据变量变化的，所以，需要一种简便的格式化字符串的方式。
# 在Python中，采用的格式化方式和C语言是一致的，用%实现，举例如下：
print()
