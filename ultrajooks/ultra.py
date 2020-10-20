import datetime

f = open("ultrajooks/ultrasis.txt", "r")

a = int(f.readline())

dict1 = {}

def converter(test):
    time = test.split(':')
    hours = int(time[0]) * 3600
    minutes = int(time[1]) * 60
    seconds = int(time[2]) + minutes + hours
    return int(seconds)

def reverseConv(test):
    hours = int(test)/ 3600
    minutes = int(hours) % 3600 / 60
    seconds = int(hours) % 3600 % 60
    print (str(int(hours)) + ":" + str(int(minutes)) + ":" + str(int(seconds)))

for line in range(a):
    data = f.readline().strip('\n')
    line = data.split(",")
    if len(line) == 5:
        team = line[4]
        if line[2] == 'DQ':
            line[3] = '00:00:00'
        if team not in dict1:
            dict1[team] = {
                'time': converter(line[3]),
                'distance' : line[2],
                'gender' : line[1]
            }

        else:
            dict1[team]['time'] += converter(line[3])
        reverseConv(dict1[team]['time'])

print(dict1)
