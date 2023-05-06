list1 = [5,4,3,2,1]
list2 = ["kela", "apple", "mango","santra"]
'''
#will print element of list1 followed by list2
list1.extend(list2)
print(list1)

#to add elements
list2.append("cherry")
print(len(list2))

#want to add element at specific position
list2.insert(1,"banana")
print(list2)
'''

#to remove element
list2.remove("kela")
print(list2)

'''

#to delete entire list
list2.clear()
print(list2)#null []'''

#index of specific element in the list
print(list2.index('mango'))

#to check how many time value is repeating
print(list2.count("santra"))#1

#sort the list
list1.sort()
print(list1)#[1,2,3,4,5]

#to reverse
list2.reverse()
print(list2)

#to copy the element of the list to the same list
list3 = list2.copy()
print(list3)

#delete elemet at specific index
del list2[0]
print(list2)

'''
#delete entire list
del list2
print(list2) # error not defined'''







