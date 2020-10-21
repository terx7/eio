import datetime
import time

f = open("ultrajooks/ultrasis.txt", "r")

a = int(f.readline())

dict1 = {}

def converter(test):
    h, m, s = test.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def reverseConv(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    print(hour, min, sec)
    return "%d:%02d:%02d" % (hour, min, sec)


for line in range(a):
    data = f.readline().strip('\n')
    line = data.split(",")
    if len(line) == 5:
        team = line[4]
        if line[2] == 'DQ':
            line[3] = '00:00:00'
        if team not in dict1:
            dict1[team] = {
                'mTime' : [],
                'nTime' : [],
                'distance' : {
                },
                }
        dict1[team]['distance'][converter(line[3])] = line[2]
        if line[1] == "M":
            dict1[team]['mTime'].append(converter(line[3]))
        else:
            dict1[team]['nTime'].append(line[3])



        #else:
            #dict1[team]['time'] += converter(line[3])

#for x in dict1:
   # reverseConv(dict1[x]['time'])
print(dict1)
