from builtins import range
num = int(input("Enter highest number"))
last = 3
result = []
for i in range(3, num + 1):
    for x in range(2, int(i/3) + 1):
        if(i%x == 0):
            break
    else:
        if(i-2 == last):
            result.append(last)
            result.append(i)
        last = i
for i in range(0, len(result) -1, 2):
    print(result[i], end=',')
    print(result[i+1], end=' ')
