import random
import string

# Get the desired password length from the user
length = int(input("Enter password length: "))

# Combine letters, digits, and symbols
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password using a list comprehension and join
password = "".join(random.choice(characters) for _ in range(length))

# Print the final result
print("Your generated password is:", password)

input("any input to close.")