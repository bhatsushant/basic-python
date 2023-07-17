# Sets
# Creating Sets
print("Creating sets".center(50, "="))
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
nums3 = {1, 2, 2, 3}           # Will remove duplicates

# 1 == True and 0 == False
nums4 = {1, True, 2, False, 3, 4, 0}

print(nums)
print(nums2)
print(nums3)                    # No duplicates in this set
print(nums4)
print(type(nums))
print(len(nums2))

print("")

# Set elements canot be referred to by their index positions

# Adding new elements to sets
print("Adding new elements to sets".center(50, "="))
print("")
nums.add(8)
print(nums)

print("")
# Adding elements from one set to another
print("Adding elements from one set to another".center(50, "="))
print("")
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# lists, tuples and dictionaries can also be passed in the update method of sets
nums.update([9, 10])
print(nums)
nums.update((-1, -2))
print(nums)

print("")
# Merge two sets to create a new set
print("Merge two sets to create a new set".center(50, "="))
print("")
one = {1, 2, 3}
two = {5, 6, 7}
myset = one.union(two)
print(myset)

print("")
# More set methods
print("More set methods".center(50, "="))
print("")
one = {1, 2, 3}
two = {2, 3, 4}
print(one)
print(two)

# Return the intersection of two sets as a new set. (i.e. all elements that are in both sets.)
three = one.intersection(two)
print(three)

# Return the symmetric difference of two sets as a new set. (i.e. all elements that are in exactly one of the sets.)
four = one.symmetric_difference(two)
print(four)

# Return the difference of two or more sets as a new set (i.e. all elements that are in this set but not the others.)
five = one.difference(two)
print(five)

# Return the difference of two or more sets as a new set (i.e. all elements that are in this set but not the others.)
six = two.difference(one)
print(six)
