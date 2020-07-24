# Problem 3 : Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# 問題 3 : 最大素因数
# 13195の素因数は5, 7, 13, 29である．
# 600851475143の最大の素因数はいくらか？

i = 2
composite_number = 600851475143
prime_list = []
flag = 0

while composite_number / i != 1:
    if composite_number % i == 0:
        prime_list.append(i)
        composite_number = composite_number / i
        i = 2
    if composite_number / (i + 1) == 1:
        prime_list.append(i + 1)
    i += 1

print(prime_list[-1])