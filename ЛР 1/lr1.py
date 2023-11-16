import random
import string

def generate_password(length=8):
    
    length = max(length, 4)
    
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits

    all_characters = lowercase_letters + uppercase_letters + digits

    first_char = random.choice(string.ascii_letters)
    password = first_char + ''.join(random.choice(all_characters) for _ in range(length - 1))

    return password

n = int(input("Enter symbols count: "))

generated_password = generate_password(n)
print(generated_password)