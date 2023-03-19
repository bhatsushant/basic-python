# List Slicing

cart = ['book', 'candy', 'glasses', 'fruits']

print(cart[1:3])    # Will print from index 1 till 2 (will stop at index 3)

print(cart[::-1])

new_cart = cart[:]  # Creates a copy
new_cart[0] = 'gum'
print(new_cart)
print(cart)         # Value of first item in cart will not be changed

new_cart = cart
new_cart[0] = 'gum'
print(new_cart)
print(cart)         # Value of first item in cart will also be changed as new_cart = cart