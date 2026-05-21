def lestrotatearr(lst):
    val=lst.pop(0)
    lst.append(val)
    return lst
lst=eval(input("Enter the list :"))
res=lestrotatearr(lst)
print(res)