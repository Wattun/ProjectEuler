# Problem 3 : Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# 問題 3 : 最大素因数
# 13195の素因数は5, 7, 13, 29である．
# 600851475143の素因数はいくらか？

i = 2
Composite_number = 600851475143
prime_list = []
flag = 0

while Composite_number / i != 1:
    if Composite_number % i == 0:
        prime_list.append(i)
        Composite_number = Composite_number / i
        i = 2
    if Composite_number / (i + 1) == 1:
        prime_list.append(i + 1)
    i += 1

print(prime_list[-1])
'''
def prime(self, number):
    while flag == 1:
        if number % i == 0:
            number = number / i
            prime_list.append(i)
            prime(number)
            if number / i == 1:
                flag = 1
        
        i += 1

prime(Composite_number)

print(prime_list[-1])
'''