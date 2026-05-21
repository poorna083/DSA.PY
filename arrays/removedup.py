def removedup(lst):
    val=0
    for i in range(1,len(lst)):
        if lst[val]!=lst[i]:
            val+=1
            lst[val]=lst[i]
        
    return lst

lst=eval(input("Enter the list :"))
res=removedup(lst)
print(res)

# output:
# Enter the list :[1,1,1,2,2,3,3,3,3,4,5]
# [1, 2, 3, 4, 5, 3, 3, 3, 3, 4, 5]


def removedup(lst):
    val=0
    for i in range(1,len(lst)):
        if lst[val]!=lst[i]:
            val+=1
            lst[val]=lst[i]
        
    return lst[:val+1]

lst=eval(input("Enter the list :"))
res=removedup(lst)
print(res)


# output:
# Enter the list :[1,1,1,2,2,2,3,3,4,4,5]
# [1, 2, 3, 4, 5]