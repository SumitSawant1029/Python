from collections import Counter


q1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
q2 = ['e','t','a','o','i','n','s','h','r','d','i','c','u']

string="iwoo xqjg bkn haypqnao pkzwu"
keys =[]
string1=string
string1=string1.replace(" ","")

# Find the highest Alphabet
result= Counter(string1)
result= max(result, key=result.get)
print("Most frequent character: ",result)

#Find the Index Of the largest occuring alphabet in q2 list
index1 = q1.index(str(result))

# Finding the keys difference between the charater and 
for j in range(0,len(q2)):
    index2 = q1.index(q2[j])
    key = index2 - index1
    keys.append(key)

l3=[]
# For Some Adjustments
Adjustments=input("Enter some adjustments (Enter 0 is no):")
# Convert String to list
string2=list(string)

i=0
for j in range(0,len(q2)):
    for i in range(0,len(string2)):
        if string2[i] != ' ':
            te = int(q1.index(string2[i])) - keys[j] + int(Adjustments)

            l3.append(q1[te%26])
        else:
            l3.append(' ')      

    # Convert the array to a string with a specified separator
    separator = ''  # Choose the separator you want between elements
    result_string = separator.join(map(str, l3))
    print(q2[j],end="")
    print(":-",end="")
    print(result_string)

    l3.clear()
