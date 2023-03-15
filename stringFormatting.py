# String formatting

# string formatting using the 'f' keyword
name = 'Sushant'
age = 29

print(f'Name: {name} \t Age: {age}')

# string formatting using the 'format()' method
print('Name: {} \t Age: {}'.format(name, age))

print('Name: {} \t Age: {}'.format('Sushi', 29))

# string formatting using the 'format()' method with positional arguments
print('Name: {new_name} \t Age: {new_age}'.format(new_name = 'Sush', new_age = 28))

# string formatting using the 'format()' method - interchanging arguments using indexes
print('Name: {1} \t Age: {0}'.format(name, age))

print('Name: {1} \t Age: {0}'.format('Sushi', 29))

