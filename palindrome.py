# WAP TO CHECK WHEATHER THE GIVEN NUMBER IS A PALINDROME OR NOT
no = int(input("Enter the number :"))
temp = no
num = 0
while no>0:                    
    rem = no%10                
    num = num*10+rem             
    no = no//10               
if temp == num:
    print("armstrong number")
else:
    print("not an armstrong number")