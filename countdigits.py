# count the digits

num = int(input("enter the value:"))

count = 0

while num>0:
   num= num//10
   count+=1

print(count)