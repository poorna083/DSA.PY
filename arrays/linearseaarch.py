def linearsearch(arr,num):
    for i in range(len(arr)):
        if arr[i]==num:
            return i
        
arr=eval(input("Enter the array :"))
num=int(input("Enter the target :"))
res=linearsearch(arr,num)
print(res)