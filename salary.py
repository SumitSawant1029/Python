#program to Calculate Monthly Salary
e=0
month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
salary_per_day=3000
def salary1(a,b):
    hrs = int(salary_per_day / 24)
    salary = a * salary_per_day + b * hrs
    return salary

while e==0:
    print('******************************************')
    print('1)Calculate Salary\n2)Set Salary per day\n2)Exit')
    ch = int(input('Enter Your Choice:-'))
    print('******************************************')
    if ch==1:
        b=0

        while b == 0:
            month1 = int(input('Enter The Month No:-'))
            if 0 < month1 < 13:
                absent = int(input('Enter No Of Absent days:-'))
                overtime = int(input('Enter Overtime hrs:-'))
                present_days = month[month1]-int(absent)
                print('Your Total Salary is :-',salary1(present_days,overtime))
                b = 1
            else :
                print('Enter Valid Month No')

    elif ch ==2:
        salary_per_day = int(input('Enter Salary per Day:-'))
    elif ch==3:
        e=1
    else :
        print('You Entered Wrong Choice ! Please Try Again')
