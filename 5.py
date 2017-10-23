# 条件判断
age = 20
print('Your age is: ', age)
if age >= 18:
    print('You are an adult')
elif age >= 6:
    print('You are a teenager')
else:
    print('You are a kid')

# 循环
# for...in
sum1 = 0
for x in range(101):
    sum1 = sum1 + x
print(sum1)

# while
sum2 = 0
n = 99
while n > 0:
    sum2 = sum2 + n
    n = n - 2
print(sum2)

# break
# 在循环中，break语句可以提前退出循环
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')

# continue
# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
