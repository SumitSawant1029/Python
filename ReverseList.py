# Program to reverse list

L1=[]
L2=[]
size = int(input("Enter The Number of Elements :- "))
for i in range(0,size):
    ele = input("Enter The Element:-")
    L1.append(ele)
print(L1)
j=-1
for i in range(size,0,-1):
    j = j + 1
    # L2[j]=L1[i]

    print(i)
    print(j)
print(L2)
