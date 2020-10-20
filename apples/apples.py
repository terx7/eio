f = open('apples/jagasis.txt', 'r')

n = int(f.readline())
aList = []

for i in range(n):
    a = int(f.readline())
    aList.append(a)
    aSum = sum(aList)

z = round(n / 2)
print(z)
