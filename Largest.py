# Largest Element in the List

# Name :- Sumit Sandeep Sawant
L1=[]
# For Taking Inputs
size = int(input("Enter The Number of Elements:- "))
for i in range(0,size):
    num = input("Enter The Element:-")
    L1.append(num)

max = int(L1[0])

for i in range(1,size):
    if max <= int(L1[i]):
        max = int(L1[i])

print("The Las=rgest Element is ",max)
