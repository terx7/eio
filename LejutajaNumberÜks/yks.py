f = open("LejutajaNumberÜks/ykssis.txt", "r")

A = f.readline()

alist = A.split()
adalbert = int(alist[0]) + int(alist[1]) * 10

maximum = adalbert

leiutised = []
for line in f:
    data = line.split()
    math = int(data[0]) + int(data[1]) * 10
    leiutised.append(math)
    bignum = max(leiutised)
    if bignum >= adalbert:
        maximum = bignum


result = maximum - adalbert + 1
print(result)
