list1 = [45, 23, 2, 6, 43, 10, 45, 34]
for index, item in enumerate(list1):
    print(index, item)
list2 = [i for i in list1 if i < 8]
print(list2)
set1 = {i for i in list1 if i < 8}
print(set1)
num = int(input("Enter your No."))
table = {num*i for i in range(1,10)}
print(table)