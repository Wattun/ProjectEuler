# Problem 1 : Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# 問題 1 : 3もしくは5の倍数
# 10以下の自然数において3もしくは5の倍数は3, 5, 6, 9である．
# そしてそれらの合計は23である．
# 1000未満の3もしくは5の倍数の合計値を求めよ．

total = 0

for i in range(1, 1000):
    if i % 15 == 0:
        total += i
    elif i % 3 == 0:
        total += i
    elif i % 5 == 0:
        total +=i
    else:
        pass

print(total)