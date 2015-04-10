a = input("Enter first number")
b = input("Enter second number")
longer, smaller = "", ""
if(len(a) > len(b)):
    longer = a
    smaller = b
else:
    longer = b
    smaller = a
s = len(smaller) - 1
result = [""]
c = 0
for i in reversed(range(len(longer))):        
    x = int(longer[i])
    y = 0
    if(s >= 0):
        y = int(smaller[s])
        s-=1
    sum1 = x+y + c
    c = 0
    if(sum1 > 9) :
        c = 1
        sum1 -= 10
    result.append(sum1)
for i in reversed(range(len(result))):
    print(result[i], end='')