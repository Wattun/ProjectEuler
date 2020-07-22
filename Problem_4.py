import math 


# 与えられた整数が三桁の数の積か判定したかった
# 素因数分解をしてしまった
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

def judge_three_digit_product_true(num):

    devided_num = 0
    flag = False

    for i in reversed(range(100, 1000)):

        # print(num % i)
        if num % i == 0:
            devided_num = num / i

            devided_num = int(devided_num)
            #print(len(str(devided_num)))

            if len(str(devided_num)) == 3:
                flag = True
                break

    return flag
            

# 与えられた数が回文数かを判定する
def judge_circulatory_num(num):
    digit = 0
    conversed_num = 0
    temp_num = 0
    original_num = num
    flag = False

    digit = len(str(num))

    for i in range(digit):
        temp_num = num % 10
        temp_num = math.floor(temp_num)
        conversed_num += temp_num * pow(10, digit - 1 - i)
        num = num / 10
        
    if conversed_num == original_num:
        flag = True
    

    return flag


print(judge_three_digit_product_true(146376))
print(judge_circulatory_num(906609))




if judge_circulatory_num(906609) == True and judge_three_digit_product_true(906609) == True:
    print("成功")

first_num = 1000 * 1000

for first_num in reversed(range(0, first_num)):

    if judge_circulatory_num(first_num) == True and judge_three_digit_product_true(first_num) == True:
        print(first_num)
        break

'''
test = 10

for test in reversed(range(0, 10)):
    print(test)
    if test == 4:
        print(test)
        break
'''