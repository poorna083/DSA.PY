# lst=eval(input("Enter the list :"))
# count=1
# check_element=lst[0]
# for i in range(1,len(lst)):
#     if check_element <= lst[i]:
#         check_element = lst[i]
#         count+=1
# if count == len(lst):
#     print("True")
# else:
#     print("False")

# ----------------------------------------------------
lst = eval(input("Enter the list: "))

is_sorted = True

for i in range(len(lst) - 1):
    if lst[i] > lst[i + 1]:
        is_sorted = False
        break

print(is_sorted)