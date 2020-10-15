import sys



f = sys.stdin

dict1= {}
dict2 = {}
dict3 = {}
n = int(f.readline())

for i in range(n):
    name = f.readline()
    nameList = name.split()
    dict1[nameList[0]] = nameList[1]
for i in range(n):
    name2 = f.readline()
    nameList2 = name2.split()
    dict2[nameList2[0]] = nameList2[1]


for x in dict1:
        for y in dict2:
            if x == y:
                dict3[dict1[x]] = dict2[y]

for x in dict3:
    sys.stdout.write(x + " " + dict3[x] + "\n")
