import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation 
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Get user input for password length
try:
    length = int(input("Enter the length of the password you want to generate: "))
    if length <= 0:
        raise ValueError("Length must be a positive integer.")
    
    # Generate and print the password
    password = generate_password(length)
    print()
    print(f"Generated password: {password}")
    print()

except ValueError as error:
    print(f"Error: {error}. Please enter a valid positive integer for the password length.")

