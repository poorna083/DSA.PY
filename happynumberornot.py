no = int(input("Enter the number: "))

lst = []

while no != 1 and no not in lst:
    lst.append(no)

    total = 0
    temp = no

    while temp > 0:
        rem = temp % 10
        total += rem * rem
        temp = temp // 10

    no = total

if no == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")