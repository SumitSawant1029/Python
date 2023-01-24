# Name :- Sumit Sandeep Sawant

# Search For A Name In A List
L1 = ['Hendry', 'dog', 'Cat', 'Hello', 'Sumit']

find = input("Enter The Name You Wnat To Search :-")
flag=0
for i in range(0,4):
    if find == L1[i]:
        flag = 1
        break

if flag==1:
    print("Your Search is There in The list")
else :
    print("Your Search Is not Found")
