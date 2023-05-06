#You can keep different datatyes in sigle list

countries = ['UK', 'USA', 'Dubai', 'Iran', 5, True]

print(countries)
print(countries[0]) # will print UK
print(countries[2][0]) # D

#this will get from index 1 to end
print(countries[1:])

#excluds the last index means if you write 2 this will go up till 1
print(countries[0:2])

print(type(countries)) #<class 'list'>

name = 'Tom'
print(type(name)) #<class 'str'>

# -1 and -2 etc will give you char from the last
print(countries[-2])#Dubai

print(len(countries))#4 

print(type(countries[4])) #int


#we can also use list constructors by typing list(())
countries2 = list(('nagaland', 34, False))
print(type(countries2)) #list

