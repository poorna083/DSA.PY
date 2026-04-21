no=int(input("enter the number  :"))
temp = no
sum = 0
while no > 0:
    rem = no%10
    sum = sum*10+rem
    no = no//10

if temp == sum:
    print("palindrome ")
else:
    print("not a palindrome ")