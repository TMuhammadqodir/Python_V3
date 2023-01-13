list1=[2,5,1,4,3,2,1,6,8,5,7,9,7,7,7,7,5]
for i in list1:
    while list1.count(i)>1:
        list1.remove(i)
print(list1)