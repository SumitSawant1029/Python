# Python Program to Calculate library Fine
e=0
def fine(no,re):
    if int(re) == 1:
        fine1=0
    elif int(re) == 2:
        fine1=10
    else:
        fine1=20

    fine2 = int(no) * 10 + fine1
    return fine2

while e==0:
    print("1)Book Delayed\n2)Book On Time\n3)Exit")
    ch = int(input('Enter Your Choice:-'))
    if ch == 1:
        print('1)Story Book\n2)Reference Book\n3)Horror Book')
        type = input('Enter Your Choice:-')
        no_of_days =input('Enter No Of Days Delayed:-')
        print('1)Excellent\n2)Good\n3)Bad')
        condition=input('Enter Your Choice:-')
        print('Your Total Fine Is :-',fine(no_of_days,condition))
        e=1
    elif ch == 2 :
        print('1)Story Book\n2)Reference Book\n3)Horror Book')
        type = input('Enter Your Choice:-')
        print('1)Excellent\n2)Good\n3)Bad')
        condition = input('Enter Your Choice:-')
        print('Your Total Fine Is :-', fine(0, condition))
        e=1
    else:
        e=1
