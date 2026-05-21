lst=eval(input("Enter the list"))
largest_element=lst[0]
for i in range(1,len(lst)):
    if largest_element <= lst[i]:
        largest_element=lst[i]

print(largest_element)
