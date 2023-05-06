#When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

#The try block lets you test a block of code for errors.

#The except block lets you handle the error.

#finally block executes code no matter what happened in the try or except block.


'''
x = int(input("Enter an integer: "))
print(x)#if input will be string than it will produce error, so to handle such thinhs we can use try expect block
'''
'''
try:
    x = int(input("Enter an integer: "))
    print(x)
except :
    print("Not an integer")
else:
    print("Nothing went wrong")
'''

try:
    x = int(input("Enter an integer: "))
    print(x)
except :
    print("Not an integer")
finally:
    print("try except executed successfully")

