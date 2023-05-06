'''[]
#Function is a block of code which peroform particular task
#funtions allows you to package your code well
def greetings(name, age):
    print("welcome to python "+ str(name) +" \nYour age is "+str(age))

#writing greetings funtions here means we are out of funtion now
greetings("Suraj", 17)



#to use multiple arguments in single variable
def naam(*names):
    print("Welcome "+names[1])

naam("Channu", "Mannu", "Kannu")

'''
#Use of return statement
def add_numbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return num1 + num2


# by default values considered to be string
print(add_numbers())
