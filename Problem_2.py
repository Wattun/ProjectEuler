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