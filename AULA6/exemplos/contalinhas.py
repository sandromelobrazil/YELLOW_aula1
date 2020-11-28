a = open("test.txt","r")
b = a.readlines()
a.close()

count = 0
for line in b:
    count += 1
