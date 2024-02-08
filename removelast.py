str1 = 'https://www.w3resource.com/python-exercises/string'

# Use the rsplit() method with '/' as the separator to split the string from the right,
# and [0] to get the part before the last '/' character. 
print(str1.rsplit('/', 1)[0])

# Use the rsplit() method with '-' as the separator to split the string from the right,
# and [0] to get the part after the last '-' character. 
print(str1.rsplit('-', 1)[1])  
