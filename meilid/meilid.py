f = open("meilid/meilsis.txt", "r")

a = int(f.readline())

address_book = []
e_mails = 0

for line in range(a):
    mail = f.readline()
    address_book.append(mail)

b = int(f.readline())

for line in range(b):
    incomming_mail = f.readline()
    if incomming_mail in address_book:
        e_mails += 1

print(e_mails)
