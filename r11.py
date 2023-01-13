nums=[1123456,33,50]
number=int()
for i in nums:
    number=number*int('1'+'0'*len(str(i)))+i
print(number)