# Problem 5 : Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# 問題 5 : 最小の積
# 2520は1から10までの数の最小公倍数である
# 1から20までの数の最小公倍数はいくらか

# 最大公約数を求める関数
def gcd(a, b):
    
    remainder = 0
    flag = False
    GCD = 0

    if b > a:
        temp = a
        a = b
        b = temp

    while flag != True:
        remainder = a % b
        a = b
        b = remainder
    
        if remainder == 0:
            GCD = a
            flag = True
    
    return GCD

# 最小公倍数を求める関数
def lcm(a, b):
    LCM = int(a * b / gcd(a, b))
    return LCM

multiple = 1

for i in range(2, 21):
    new_multiple = lcm(multiple, i)
    multiple = new_multiple

print(multiple)