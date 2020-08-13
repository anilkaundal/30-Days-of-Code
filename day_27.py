# Enter your code here. Read input from STDIN. Print output to STDOUT
actual = input().split()
actual = list(map(int, actual))
due = input().split()
due = list(map(int, due))

fine = 0

if actual[2] > due[2]:
    fine = 10000
elif actual[2] == due[2]:
    if actual[1] > due[1]:
        fine = (actual[1] - due[1]) * 500
    elif actual[0] > due[0] and actual[1] == due[1]:
        fine = (actual[0] - due[0])* 15

print(fine)
