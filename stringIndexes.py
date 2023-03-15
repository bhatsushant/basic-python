# String Indexes

name = 'Sushant'
      # 0123456

# Will print the string from index 0 till the end
print(name[0:])

# Will print the string from index 1 till the 5 (not including 5)
print(name[1:5])

# Will print the string from index 0 till the end
print(name[0:7:1])

# Will print the string from index 0 till the end stepping over 2 indexes at a time
print(name[0:7:2])

# Will print the string from index 0 till the index specified after the first colon(not including the specified index after the colon)
print(name[:5])

# Will print the string from index 0 till the index specified after the first colon(not including the specified index after the colon) stepping over 2 indexes at a time
print(name[:5:2])

# Reverses the string
print(name[::-1])

# Reverses the string stepping over 2 indexes at a time
print(name[::-2])

