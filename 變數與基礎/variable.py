# # 基礎變數運算
# hourly_salary = 150
# day_salary = hourly_salary * 8
# week_salary = day_salary * 5

# print(week_salary)


# # 可以問Python保留字
# help("keywords")


# # 如果把內建函數拿去當變數用，同名函數就失效

# # 餘數
# x = 15 % 6

# # 最大可以整除的數
# y = 15 // 6

# print(x)
# print(y)

# # 次方
# x = 3**2
# print(x)

# # !!Python運算的優先順序
# # 1.()
# # 2.次方**
# # 3. * / % //, 左到右
# # 4. + -, 左到右


# # Python可以同時賦值多個變數
# x = y = z = 20
# print(x, y, z)

# x, y = 1, 2
# print(x, y)


# # 利率計算
# # 公式：本金和 = 本金 *（1+年利率）

# x = 50000
# y = x * ((1 + (1.5 / 100)) ** 5)

# print(y)

# # 車輛殘值
# # 某車殘值每年衰退15%，新車價100萬三年後殘值

# x = 1000000
# y = x * ((1 - (15 / 100)) ** 3)
# print(y)


# # 某圓
# r = 5
# PI = 3.1415926
# # 面積
# Area = (r**2) * PI
# # 周長
# C = 2 * PI * r

# print(Area, C)

import math

r = 5
print("圓面積：")
print(math.pi * r * r)
print("圓周長：")
print(math.pi * 2 * r)
