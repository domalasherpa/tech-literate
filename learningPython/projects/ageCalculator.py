import datetime as dt

dob = input("Enter date of birth(yyyy/mm/dd): ")

y = dob[0:4]
m = dob[5:7]    
d = dob[8:10]

dd = dt.datetime.now().strftime("%d")
mm = dt.datetime.now().strftime("%m")
yy = dt.datetime.now().strftime("%Y")

age = 0

if(int(yy) > int(y)):
    if int(mm) > int(m):
        age = int(yy) - int(y)
    elif int(mm) == int(m):
        if int(dd) >= int(d):
            age = int(yy) - int(y)
        else:
            age = int(yy) - int(y) - 1
    else:
        age = int(yy) - int(y) - 1
    print("Your age is: ",age)
elif(int(yy) == int(y)):
    print("Your age is: ",age)
else:
    print("Invalid date of birth")
