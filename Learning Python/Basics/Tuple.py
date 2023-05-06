#tuple are used to store multiple identity in single variable
#Tuples are immutable in python
#tuple allow dulicate values
#tuple allow various type of datatype in single var

#usually we use list over tuple, 
#We use tuple when we are working with co-ordinates or values that we do not want to manupulate




three_numbers = (1,2,3)
print(three_numbers[0])
'''
three_numbers[1] = 23
print(three_numbers)# error 'tuple' object does not support item assignment
'''

print(len(three_numbers)) #3

print(type(three_numbers))#tuple

