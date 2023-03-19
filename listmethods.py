# List Methods

numbers = [1,2,3,4,5]

numbers.append(6)                   # appends a new item to the list
print("APPEND-->",numbers)

numbers.extend([7,8,9,10])          # list can be extended further by providing a new list
print("EXTEND-->",numbers)

new_list = numbers.remove(4)        # removes the specified item from the list    
print("REMOVE-->",numbers)
print("REMOVE-->",new_list)         # will return 'None'

numbers.insert(3,4)                 # inserts an item at the given index
print("INSERT-->",numbers)  

# The above methods modify the list in place meaning they modify the original list and hence assigning them to a new variable will produce 'None' as shown in the above example with 'new_list'

length = len(numbers)               # computes the length of the list
print("LENGTH-->",length)

item = numbers.pop()                # pops the last item from the list
print("POP-->",numbers)
print("POP-->",item)                # will return the deleted item frm the list

new_list = numbers.clear()          # clears the entire list
print("CLEAR-->",numbers)
print("CLEAR-->",new_list)          # will return 'None' 