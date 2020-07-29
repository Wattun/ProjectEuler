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

# TODO: ピタゴラス数を判定する関数
# TODO: 3つの数の和が1000であるかどうかの判定

import math

# 2つの数がピタゴラスの式を満たすか判定する
def pythagorean_num(a, b):
    c_dash = a ^ 2 + b ^ 2
    c = 0

    if math.sqrt(c_dash).is_integer() == True:
        c = math.sqrt(c_dash)

# テスト


# ある数の平方根が整数かどうかの判定
aru_kazu = 81
print(math.sqrt(aru_kazu).is_integer())