# Problem 10 : Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# 問題 10 :  素数の総和
# 10以下の素数の和は2+3+5+7=17のようになる．
# 200万以下の全ての素数の総和を求めよ．

from tqdm import tqdm


# 素数か銅貨を判定する関数
def judge_prime_number(num):
    prime_factor = []
    temp = num
    total_cnt = 0
    flag = False

    for index in range(2, int(-(-num**0.5//1))+1):
        if temp % index == 0:
            cnt = 0
            while temp % index == 0:
                cnt += 1
                temp //= index
            prime_factor.append([index, cnt])
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

summation = 0

for index in tqdm(range(2, (10**6)*2)):
    
    if judge_prime_number(index) == True:
        summation += index

print(summation)