# Dictionaries
print("creating dictionaries".center(50, "="))
print("")
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band2))

print("")
# Accessing dictionaries
print("Accessing dictionaries".center(50, "="))
print("")
print(band["vocals"])
print(band.get("guitar"))

print("")
# List all keys
print("List all keys".center(50, "="))
print("")
print(band.keys())

print("")
# List all values
print("List all values".center(50, "="))
print("")
print(band.keys())

print("")
# List all key/value pairs as tuples
print("List all key/value pairs as tuples".center(20, "="))
print("")
print(band.items())

print("")
# Verify if key exists
print("Verify if key exists".center(50, "="))
print("")
print("guitar" in band)
print("triangle" in band)

print("")
# Changing values in dictionaries
print("Changing values in dictionaries".center(50, "="))
print("")
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

print("")
# Removing items from dictionaries
print("Removing items from dictionaries".center(50, "="))
print("")
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())       # returns a tuple
print(band)

print("")
# Delete and clear items from dictionaries
print("Delete and clear items from dictionaries".center(50, "="))
print("")
band["drums"] = "Bonham"
del band["drums"]
print(band)
band2.clear()
print(band2)
del band2           # deletes band2
# print(band2)      # Error as band2 has been deleted

print("")
# Copying dictionaries
print("Copying dictionaries".center(50, "="))
print("")
# band2 = band
# print("Bad Copy!")
# print(band2)
# print(band)
# print("")
# band2["drums"] = "Dave"
# print(band)


band2 = band.copy()
band2["drums"] = "Dave"
print("Good Copy!")
print(band)
print(band2)

# Using the dict function to create a copy
band3 = dict(band)
print("Good Copy!")
print(band)

print("")
# Nested dictionaries
print("Copying dictionaries".center(50, "="))
print("")
member1 = {
    "firstname": "Sam",
    "lastname": "Worthington"
}

member2 = {
    "firstname": "John",
    "lastname": "Doe"
}

names = {
    "member1": member1,
    "member2": member2
}

print(names)
print(names["member1"]["lastname"])
