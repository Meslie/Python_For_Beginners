import math
a = -1
b = -2
c = 3

'''
二元一次方程解
开平方的另一种写法
- b + (b ** 2 - 4 * a * c) ** (1 / 2)

math.sqrt开平方
'''

print((- b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a)
print((- b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a)