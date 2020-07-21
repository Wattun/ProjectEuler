total = 0
i = 1

for i in range(1000):
    if i % 15 == 0:
        total += i
        print(15)
    elif i % 3 == 0:
        total += i
        print(3)
    elif i % 5 == 0:
        total +=i
    else:
        pass

print(total)