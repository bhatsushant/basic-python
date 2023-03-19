# Simple password checker program

username = input("Please enter username: ")
password = input("Please provide a password: ")

print(f"Hi {username}! Your password {len(password) * '*'} is {len(password)} characters long")