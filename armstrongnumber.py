no=int(input("enter the number :"))
temp = no
temp1 = no
count =0
sum =0
while no > 0:
    count+=1
    no = no//10

while temp > 0:
    rem = temp %10
    sum += (rem**count)
    temp //=10
if temp1 == sum:
    print("armstrong number ")
else:
    print("not a amstrong number ")