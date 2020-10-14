f = open("file.txt", "r")

dict = {}
n = f.readline()

for i in range(3):
    name = f.readline()
    namesLists = name.split()
    dict[namesLists[0]] = namesLists[1]

print(dict)
