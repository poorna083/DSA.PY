no=int(input("enter the number :"))
temp1 = no
temp2 = no
count = 0

while temp1 > 0:
    count+=1
    temp1=temp1//10

sum = 0
while temp2 > 0:
    val = temp2 % 10
    sum += val**count
    temp2 = temp2//10

if sum == no:
    print("armstrong number")
else:
    print("not a armstrong number")