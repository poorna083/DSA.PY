lst=[5,6,7,7,1,9,111,1,1,5,1,1]
dict={}
for i in lst:
    if i in dict:
        dict[i] += 1
    else:
        dict[i]=1

print(dict)