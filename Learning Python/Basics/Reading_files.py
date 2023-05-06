#In Python, you can read files using the built-in open() function.

#want to read file
file = open("filename.txt", "r")

#want to write or edit in file
file = open("filename.txt", "w")

#want to append to the file
file = open("filename.txt", "a")


'''
# Open the file in read mode
file = open("filename.txt", "r")

# Read the contents of the file
content = file.read()

# Close the file
file.close()

# Print the contents of the file
print(content)'''

#It's important to remember to close the file after you are done reading it, 
#as this frees up system resources and prevents errors. Alternatively, 
#you can use a context manager to automatically close the file for you:

# Open the file using a context manager
with open("filename.txt", "r") as file:
    content = file.read()

# Print the contents of the file
print(content)




coun_file = open("file address", "r")
print(coun_file.readline())
print(coun_file.readlines())
coun_file.close()



