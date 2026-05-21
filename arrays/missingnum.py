def missingnumber(num):
    val=len(num)+1
    exp_sum=val*(val+1)//2
    sum=0
    for i in num:
        sum+=i
    
    missingnum = exp_sum-sum

    return missingnum




num=eval(input("Enter the list"))
res = missingnumber(num)
print(res)