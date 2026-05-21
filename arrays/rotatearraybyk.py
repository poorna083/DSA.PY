def rotatearray(k,lst,dir):
    if dir=="right":
        for i in range(k):
            val=lst.pop()
            lst.insert(0,val)
        
        return lst
    
    else:
        for i in range(k):
            val=lst.pop(0)
            lst.append(val)

        return lst



dir=input("Enter the direction :")
k=int(input("Enter the number of shifts :"))
lst=eval(input("Enter the list :"))
res=rotatearray(k,lst)
print(res)
