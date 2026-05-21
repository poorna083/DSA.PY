def maxconsicativeones(nums):
    max_once = 0
    count = 0
    for i in nums:
        if i == 1:
            count += 1
        else:
            if count > max_once:
                max_once = count
            count = 0
    if count > max_once:
        max_once = count

    return max_once


nums = eval(input("Enter the list : "))
res = maxconsicativeones(nums)
print(res)