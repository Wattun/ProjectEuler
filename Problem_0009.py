# Problem 9 : Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# 問題 9 : 特別なピタゴラス数
# ピタゴラス数とは下の式が成立し，a < b < cが成り立つ3つの数字である．
# a^2 + b^2 = c^2
# 例えば，3^2 + 4^2 = 9 + 16 = 25 = 5^2である．
# a + b + c = 1000となるピタゴラス数が一組だけ存在する．
# ピタゴラス数a, b, cの積abcを求めよ．

import math

# 2つの数がピタゴラスの式を満たすか判定する
# 入力(a, b)がピタゴラス数になりうる場合は残りの数字cを返す．
def pythagorean_num(a, b):
    c_dash = a ** 2 + b ** 2
    c = 0

    if math.sqrt(c_dash).is_integer() == True:
        c = int(math.sqrt(c_dash))

    return c

# ピタゴラス数の判定が出た際に合計が1000になるかどうかの判定
def judge_total_thousand(a, b, c):

    if a + b + c == 1000:
        return True
    else:
        return False


for a_index in range(1, 500):
    for b_index in range(1, 500):
        c_index = pythagorean_num(a_index, b_index)
        if (c_index != 0) and judge_total_thousand(a_index, b_index, c_index):
            print("Special Pythagorean triplet is \n")
            print("a =",a_index, "b =",b_index, "c =", c_index)
            print("a*b*c=", a_index * b_index * c_index)
            break
    
    else:
        continue
    break