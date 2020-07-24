# Problem 6 : Sum square difference
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# 問題 6 : 和の二乗の差
# 自然数の最初の10個の二乗の和は，
# 1^2 + 2^2 + ... + 10^2 = 385
# 自然数の最初の10個の和の二乗は，
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# よって自然数の10個の二乗の和と10個の和の二乗の差は
# 3025 - 385 = 2640
# 自然数の100個の和の二乗と100個の二乗の和の差を求めよ．

import numpy as np

# 1から100までのNumpy配列を用意
sequence = np.arange(1, 101)
# 平方の和
sum_of_suquare = np.sum(sequence ** 2)
# 和の平方
square_of_sum = np.sum(sequence) ** 2

# 和の平方から平方の和を引いた数
sum_square_difference = square_of_sum - sum_of_suquare

print(sum_square_difference)