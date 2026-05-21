lst=eval(input("Enter the string :"))
smallest_element=lst[0]
largest_element=lst[0]
for i in range(1,len(lst)):
    if smallest_element > lst[i]:
        smallest_element = lst[i]
    
    if largest_element <= lst[i]:
        largest_element = lst[i]

for i in range(len(lst)):
    if smallest_element < lst[i] and lst[i] < largest_element:
        smallest_element = lst[i]

print(smallest_element)