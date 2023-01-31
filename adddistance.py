#Program to add two distances given in feet and inches

d1f = int(input('Enter Distance 1 feet:-'))
d1i=int(input('Enter Distance 1 inches:-'))
d2f = int(input('Enter Distance 2 feet:-'))
d2i=int(input('Enter Distance 2 inches:-'))

inches = d1i + d2i

if 200 > inches > 100 :
    carry = 1
    inches = inches - 100
elif 300 > inches > 200 :
    carry = 2
    inches = inches - 200
elif 400 > inches > 300 :
    carry = 3
    inches = inches - 300
elif 500 > inches > 400 :
    carry = 4
    inches = inches - 400
elif 600 > inches > 500 :
    carry = 5
    inches = inches - 500
elif 700 > inches > 600 :
    carry = 6
    inches = inches - 600
elif 800 > inches > 200 :
    carry = 7
    inches = inches - 700
elif 900 > inches > 200 :
    carry = 8
    inches = inches - 800
elif 1000 > inches > 200 :
    carry = 9
    inches = inches - 900
feet = d1f + d2f + carry

print('Addition of two distances is :- ',feet,'.',inches)
