# Problem 7 : 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

# 問題 7 : 10001番目の素数
# 初めから6個の素数を列挙すると，6番目の素数は13であることが確認できる．
# 10001番目の素数は何か？

def judge_prime_number(num):
    prime_factor = []
    temp = num
    total_cnt = 0
    flag = False

    for i in range(2, int(-(-num**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            prime_factor.append([i, cnt])
            total_cnt += cnt
    
    if temp != 1:
        prime_factor.append([temp, 1])
        total_cnt += 1

    if prime_factor == []:
        prime_factor.append([n, 1])
        total_cnt += 1

    if len(prime_factor) == 1 and total_cnt == 1:
        flag = True
    

    return flag

flag = False
i = 2
count = 0

while flag != True:
    
    if judge_prime_number(i) == True:
        count += 1
    
    if count == 10001:
        print(i)
        flag = True

    i += 1