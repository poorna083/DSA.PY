def movezerolast(nums):
    res=[]
    count=0
    for i in nums:
        if i != 0:
            res.append(i)
        else:
            count+=1

    for i in range(count):
        res.append(0)

    return res


nums = eval(input("Enter the list : "))
res = movezerolast(nums)
print(res)