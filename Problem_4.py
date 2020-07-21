# 関数 1： 回文数を判定する
# 関数 2： 三桁の積か判定する

def judge_three_digit_product(num):
    prime_factor = []
    temp = num
    flag = False

    for i in range(2, int(-(-num**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            prime_factor.append([i, cnt])
    
    if temp != 1:
        prime_factor.append([temp, 1])

    if prime_factor == []:
        prime_factor.append([n, 1])

    if len(prime_factor) == 2:
        if len(str(prime_factor[0][0])) == 3 and len(str(prime_factor[1][0])) == 3:
            flag = True

    return flag

def judge_circulatory_num(num):
    digit = 0
    conversed_num = 0
    temp_num = 0
    flag = False

    digit = len(str(num))

    for i in range(digit):
        temp_num = num % 10
        conversed_num += temp_num * pow(10, digit - 1)
        
    if conversed_num == num:
        flag = True
    
    print(digit)
    print(conversed_num)
    return flag


print(judge_three_digit_product(34189))
print(judge_circulatory_num(1001))