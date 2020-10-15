f = open("tul/tulsis0.txt", "r")


n = int(f.readline())
print(n)
people = {}

for i in range(n):
    per = f.readline()
    perList = per.split()
    nameList = perList[0]
    if nameList[0] not in people:
        people[nameList[0]] = {}
