file=open("abc.txt","r")

print(file.readline())

for line in file:
    print(line)

file.close()