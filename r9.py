n=int(input('list size: '))
list1=list()
for i in range(n):
    list1.append(int(input(f'list{[i]}=')))
list1.remove(max(list1))
print('2-max in list: {}'.format(max(list1)))
