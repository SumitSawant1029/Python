# Program to interchange first and last element in a list

L1=[]

size = int(input("Enter The Number of Elements :- "))
for i in range(0,size):
    ele = input("Enter The Element:-")
    L1.append(ele)
print('Before Swapping :-',end='')
print(L1)

 #swaping
temp = L1[0]
L1[0] = L1[size-1]
L1[size-1]= temp
print('After Swapping :-',end='')
print(L1)
