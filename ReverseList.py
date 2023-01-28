# Program to reverse list

L1=[]
L2=[]
size = int(input("Enter The Number of Elements :- "))
for i in range(0,size):
    ele = input("Enter The Element:-")
    L1.append(ele)
print(L1)

for i in range(0,size):
    j = size - 1 - i
    L2.append(L1[j])
print(L2)
