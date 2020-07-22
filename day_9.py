# Enter your code here. Read input from STDIN. Print output to STDOUT 

phoneBook = {}
n = int(input())
for i in range(n):
    value = input().split()
    phoneBook[value[0]] = phoneBook.get(value[0],value[1])

while 1:
    try:
        query = input()
        if query in phoneBook:
            print(str(query) + "=" + str(phoneBook[query]))
        else:
            print("Not found")
    except:
        break
