# Program to interchange first and last element in a list

L1=[]

size = int(input("Enter The Number of Elements :- "))
for i in range(0,size):
    ele = input("Enter The Element:-")
    L1.append(ele)
print(L1)
n1 = int(input("Enter The Position:-"))
n2 = int(input("Enter The Other Position:-"))

if(n1==n2):
    print(L1)
else:
    temp = L1[n1-1]
    L1[n1-1]=L1[n2-1]
    L1[n2-1]=temp
    print("Your New List Is ",end="")
    print(L1)
