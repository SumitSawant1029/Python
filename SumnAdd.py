# Name :- Sumit Sandeep Sawant
L1=[]
# For Taking Inputs
size = int(input("Enter The Number of Elements:- "))
for i in range(0,size):
    num = input("Enter The Element:-")
    L1.append(num)
sum = 0
# For Sum of List Elements
for i in range(0,size):
    sum= sum + int(L1[i])

#For Average of List Elements
avg = sum/size

print("Average of List Elements :-",avg)
print("Sum of List Elements :-",sum)
