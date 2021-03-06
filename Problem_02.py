# Problem 2 : Even Fibonacci numbers
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
 
# 問題 2 : 偶数のフィボナッチ数
# フィボナッチ数列とは，前の2項を足すことで新たな項を生成する数列である．1と2から始めた時，10項目までは以下のようになる : 
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 400万未満の偶数のフィボナッチ数の和を求めよ．

first = 1
second = 2
total = 0

while second < 4000000:
    sum = first + second
    
    if second % 2 == 0:
        total += second
    
    first = second
    second = sum

print(total)

# 4613732