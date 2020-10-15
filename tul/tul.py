f = open("tul/tulsis0.txt", "r")


n = int(f.readline())
print(n)
people = {
    'firstName' : {

    }
}

for i in range(n):
    per = f.readline()
    perList = per.split()
    firstName = perList[0]
    if firstName not in people:
